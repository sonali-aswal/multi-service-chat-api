# Backend Service Assignment

## Overview

This project is a backend application developed using FastAPI. It exposes APIs for retrieving weather information, stock market data, and news articles. In addition, it provides a chatbot endpoint that accepts user queries and returns responses based on the available services.

The goal of the project is to demonstrate API design, external service integration, request validation, exception handling, and clean project organization.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Requests
* yfinance
* OpenWeather API
* NewsAPI

## Project Structure

* `controllers/` contains API endpoints.
* `models/` contains request models used for validation.
* `exceptions/` contains global exception handling logic.
* `main.py` is the application entry point.

## Setup Instructions

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add the required API keys:

```env
OPENWEATHER_API_KEY=your_key
NEWS_API_KEY=your_key
```

4. Start the application:

```bash
python -m uvicorn main:app --reload
```

## API Endpoints

### Weather API

**Endpoint**

GET /api/weather

**Query Parameter**

- location (string)

**Example**

GET /api/weather?location=Delhi

Returns current weather information for the specified city.

---

### Stock API

**Endpoint**

GET /api/stocks

**Query Parameter**

- ticker (string)

**Example**

GET /api/stocks?ticker=AAPL

Returns stock information for the specified company.

---

### News API

**Endpoint**

GET /api/news

**Query Parameter**

- query (string)

**Example**

GET /api/news?query=AI

Returns recent news articles related to the provided topic.

---

### Chat API

**Endpoint**

POST /api/chat

**Request Body**

{
  "message": "weather in Delhi"
}

Returns a natural language response generated from the weather, stock, or news services.

## API Documentation

Interactive API documentation is available through Swagger:

```text
http://127.0.0.1:8000/docs
```

## Design Decisions

* FastAPI was chosen because it provides automatic request validation and API documentation.
* Controllers were separated by feature to keep the code organized and maintainable.
* The chatbot uses simple keyword-based intent detection to route requests to weather, stock, and news services.
