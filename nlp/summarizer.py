from transformers import pipeline
from nlp.translator import translate_to_english

_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device_map="auto", offload_folder="offload")
    return _summarizer

def generate_summary(text, lang):
    if lang != 'en':
        text = translate_to_english(text)
    summarizer = get_summarizer()
    summary = summarizer(text[:1024])
    word_count=len(text.split())
    token_estimate = int(word_count * 0.75)

    # Dynamically calculate max/min within safe bounds
    max_len = min(350, max(30, token_estimate))
    min_len = min(100, max(20, int(max_len * 0.5)))

    summary = summarizer(
        text[:1024],  # Truncate overly long input
        min_length=min_len,
        max_length=max_len,
        do_sample=False
    )
    
    return summary[0]['summary_text']
