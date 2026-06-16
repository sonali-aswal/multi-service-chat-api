import os
import requests

from dotenv import load_dotenv
from fastapi import APIRouter

load_dotenv()

router = APIRouter()

API_KEY = os.getenv("NEWS_API_KEY")

@router.get("/api/news")
def get_news(query: str):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&apiKey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = []

    for article in data.get("articles", [])[:5]:

        articles.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name")
        })

    return {
        "query": query,
        "articles": articles
    }