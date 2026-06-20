from fastapi import FastAPI

from controllers.chat_controller import router as chat_router
from controllers.groq_chat_controller import router as groq_chat_router
from controllers.news_controller import router as news_router
from controllers.stock_controller import router as stock_router
from controllers.weather_controller import router as weather_router

from exceptions.global_exception_handler import (
    generic_exception_handler
)

app = FastAPI()

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(weather_router)
app.include_router(stock_router)
app.include_router(news_router)
app.include_router(chat_router)
app.include_router(groq_chat_router)


@app.get("/")
def home():
    return {
        "message": "Backend Assignment Running"
    }