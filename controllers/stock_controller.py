from fastapi import APIRouter, HTTPException
import yfinance as yf

router = APIRouter()


@router.get("/api/stocks")
def get_stock(ticker: str):

    if not ticker.strip():
        raise HTTPException(
            status_code=400,
            detail="Ticker symbol is required"
        )

    try:
        stock = yf.Ticker(ticker.upper())

        info = stock.info

        price = info.get("currentPrice")

        if price is None:
            raise HTTPException(
                status_code=404,
                detail=f"Stock ticker '{ticker}' not found"
            )

        return {
            "ticker": ticker.upper(),
            "company": info.get("longName"),
            "price": price,
            "currency": info.get("currency")
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching stock data: {str(e)}"
        )