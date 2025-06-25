from transformers import pipeline

_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
    return _classifier

def analyze_sentiment(text, lang):
    classifier = get_classifier()
    result = classifier(text[:512])[0]
    return f"{result['label']} ({result['score']:.2f})"
