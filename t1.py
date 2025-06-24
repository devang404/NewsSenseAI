from scraper.news_fetcher import get_article_text
article = get_article_text("https://www.bbc.com/news/world-us-canada-65823877")
print(article[:500])  # first 500 chars
from utils.language_detector import detect_language
print(detect_language(article))
from nlp.summarizer import generate_summary
print(generate_summary(article, "en"))
from nlp.sentiment_analyzer import analyze_sentiment
print(analyze_sentiment(article, "en"))
