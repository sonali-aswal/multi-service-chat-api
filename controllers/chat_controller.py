from fastapi import APIRouter

from models.chat_model import ChatRequest

from controllers.weather_controller import get_weather
from controllers.stock_controller import get_stock
from controllers.news_controller import get_news

router = APIRouter()


@router.post("/api/chat")
def chat(request: ChatRequest):

    message = request.message.strip()
    message_lower = message.lower()

    try:

        # WEATHER
        if "weather" in message_lower:

            location = "Delhi"

            if " in " in message_lower:
                location = message_lower.split(" in ", 1)[1].strip()

            weather = get_weather(location)

            return {
                "response": (
                    f"The weather in {weather['location']} is "
                    f"{weather['condition']} with a temperature of "
                    f"{weather['temperature']}°C and humidity "
                    f"{weather['humidity']}%."
                )
            }

        # STOCK
        elif "stock" in message_lower or "price" in message_lower:

            ticker = (
                message
                .replace("stock", "")
                .replace("Stock", "")
                .replace("price", "")
                .replace("Price", "")
                .replace("of", "")
                .strip()
                .upper()
            )

            if not ticker:
                return {
                    "response": (
                        "Please provide a stock ticker. "
                        "Example: stock AAPL"
                    )
                }

            stock = get_stock(ticker)

            return {
                "response": (
                    f"{stock['company']} "
                    f"({stock['ticker']}) "
                    f"is currently trading at "
                    f"{stock['price']} "
                    f"{stock['currency']}."
                )
            }

        # NEWS
        elif "news" in message_lower:

            query = (
                message_lower
                .replace("news", "")
                .replace("about", "")
                .strip()
            )

            if not query:
                query = "technology"

            news = get_news(query)

            if not news["articles"]:
                return {
                    "response": f"No news found for '{query}'."
                }

            headlines = []

            for article in news["articles"][:3]:
                headlines.append(article["title"])

            return {
                "response": (
                    f"Top news about {query}: "
                    + " | ".join(headlines)
                )
            }

        return {
            "response": (
                "Please ask about weather, stock prices, or news."
            )
        }

    except Exception as e:

        return {
            "response": f"Error processing request: {str(e)}"
        }