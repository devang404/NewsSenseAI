import requests
from bs4 import BeautifulSoup

def get_article_text(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all('p')
        article = " ".join([p.get_text() for p in paragraphs])
        return article
    except Exception as e:
        return f"Error fetching article: {e}"
