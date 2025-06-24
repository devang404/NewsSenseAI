from scraper.news_fetcher import get_article_text

url = "https://www.bbc.com/news/world-us-canada-65823877"
article = get_article_text(url)
print("Article length:", len(article))
print(article[:300])
