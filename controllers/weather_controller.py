import os
import requests

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException

load_dotenv()

router = APIRouter()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


@router.get("/api/weather/{location}")
# @router.get("/api/weather")
def get_weather(location: str):

    if not API_KEY:
        raise HTTPException(
            status_code=500,
            detail="OpenWeather API key not found"
        )

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={location}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    print("API KEY:", API_KEY)
    print("RESPONSE:", data)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=data.get("message", "Weather API error")
        )

    return {
        "location": location,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"]
    }