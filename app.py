import spacy
import stanza
from flask import Flask, render_template, request
from scraper.news_fetcher import get_article_text
from nlp.summarizer import generate_summary
from nlp.sentiment_analyzer import analyze_sentiment
from utils.language_detector import detect_language
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import re
app = Flask(__name__)
# Load spaCy models
spacy_models = {
    'en': spacy.load("en_core_web_sm"),
    'fr': spacy.load("fr_core_news_sm")
}

# Download and load stanza models for Hindi, Marathi
stanza.download('hi')
stanza.download('mr')
stanza_models = {
    'hi': stanza.Pipeline(lang='hi', processors='tokenize,ner'),
    'mr': stanza.Pipeline(lang='mr', processors='tokenize,ner')
}
def extract_entities_multilingual(text, lang_code):
    entities = {"PERSON": [], "ORG": [], "GPE": [], "DATE": []}

    if lang_code in spacy_models:
        doc = spacy_models[lang_code](text)
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent.text)

    elif lang_code in ["hi", "mr"]:
        # Use IndicNER model
        entities = extract_entities_indic_ner(text)

    elif lang_code in stanza_models:
        doc = stanza_models[lang_code](text)
        for sent in doc.sentences:
            for ent in sent.ents:
                label_map = {
                    "PERSON": "PERSON",
                    "ORG": "ORG",
                    "GPE": "GPE",
                    "LOC": "GPE",
                    "DATE": "DATE"
                }
                label = label_map.get(ent.type, None)
                if label:
                    entities[label].append(ent.text)

    for key in entities:
        entities[key] = list(set(entities[key]))

    return entities


# Setup the Indic NER model from Hugging Face
indic_ner_pipeline = pipeline(
    "ner",
    model="ai4bharat/IndicNER",
    tokenizer="ai4bharat/IndicNER",
    aggregation_strategy="simple"  # Group into full entity phrases
)

def extract_entities_indic_ner(text):
    raw_entities = indic_ner_pipeline(text)

    entities = {"PERSON": [], "ORG": [], "GPE": [], "DATE": []}

    for ent in raw_entities:
        label = ent.get("entity_group", "")
        word = ent.get("word", "").replace("##", "").strip()

        # Normalize entity group
        if not word or len(word) <= 1:
            continue  # Skip short/irrelevant pieces

        if label == "PER":
            entities["PERSON"].append(word)
        elif label == "ORG":
            entities["ORG"].append(word)
        elif label == "LOC":
            entities["GPE"].append(word)
        elif label == "DATE":
            entities["DATE"].append(word)

    # Deduplicate & clean further
    for key in entities:
        entities[key] = sorted(set([e.strip() for e in entities[key] if len(e.strip()) > 1]))

    return entities


def highlight_entities(article, entities):
    colors = {
        "PERSON": "#ffeeba",  # Light yellow
        "ORG": "#c3e6cb",     # Light green
        "GPE": "#bee5eb",     # Light blue
        "DATE": "#f5c6cb",    # Light pink
    }

    # Sort entities by length (to avoid nested replacements)
    all_entities = []
    for label, words in entities.items():
        for word in words:
            all_entities.append((label, word))

    all_entities.sort(key=lambda x: -len(x[1]))  # longer first

    # Replace each entity in the article
    for label, word in all_entities:
        pattern = re.escape(word)
        colored = f'<mark style="background-color: {colors[label]}; padding: 2px 4px; border-radius: 4px;">{word}</mark>'
        article = re.sub(pattern, colored, article)

    return article


@app.route('/', methods=['GET', 'POST'])
def index():
    article = summary = sentiment = lang = ""
    entities={}
    
    if request.method == 'POST':
        url = request.form['url']
        try:
            print("Fetching article...")
            article = get_article_text(url)
            print("Got article:", article[:300])

            lang = detect_language(article)
            print("Detected language:", lang)

            summary = generate_summary(article, lang)
            print("Generated summary:", summary[:300])

            sentiment = analyze_sentiment(article, lang)
            print("Sentiment result:", sentiment)
            
            entities = extract_entities_multilingual(article, lang)
            
        except Exception as e:
            print("❌ ERROR:", e)
            article = summary = sentiment = "Error occurred"
            lang = "unknown"
        
    return render_template('index.html',
                           article=article,
                           summary=summary,
                           sentiment=sentiment,
                           lang=lang,
                           entities=entities)



if __name__ == '__main__':
    app.run(debug=True)
