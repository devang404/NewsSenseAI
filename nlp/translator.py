from transformers import pipeline

_translator = None

def get_translator():
    global _translator
    if _translator is None:
        _translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")  # multi to English
    return _translator

def translate_to_english(text):
    translator = get_translator()
    translated = translator(text[:512])
    return translated[0]['translation_text']
