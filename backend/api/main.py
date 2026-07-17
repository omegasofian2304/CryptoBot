"""
Author : Sofian Hussein
Date : 16.07.2026
Project : CryptoBot
Desc : Create the api
"""
import requests
from fastapi import FastAPI, HTTPException

from backend.core.analyzer import get_trend
from backend.services.binance_api import get_candles

app = FastAPI()

VALID_INTERVALS = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]

@app.get("/candles")
def candles(symbol: str = "BTCUSDT", interval: str = "1h", limit: int = 100):
    try:
        if interval not in VALID_INTERVALS:
            raise HTTPException(status_code=400, detail=f"Invalid interval. Accepted values : {VALID_INTERVALS}")

        if limit > 1000000:
            raise HTTPException(status_code=400, detail="Limit must be under 1 million")

        if limit < 5:
            raise HTTPException(status_code=400, detail="Limit must be more than 5")

        candle_fetch = get_candles(symbol, interval, limit)
    except ConnectionError:
        raise HTTPException(status_code=500, detail="Server error")

    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=400, detail="Please enter valid symbol")

    return candle_fetch


@app.get("/trend")
def trend(symbol: str, interval: str = "1h", limit: int = 1000):
    try:
        if interval not in VALID_INTERVALS:
            raise HTTPException(status_code=400, detail=f"Invalid interval. Accepted values : {VALID_INTERVALS}")

        if limit > 1000000:
            raise HTTPException(status_code=400, detail="Limit must be less than 1 million")

        if limit < 5:
            raise HTTPException(status_code=400, detail="Limit must be more than 5")

        candles_fetch = get_candles(symbol, interval, limit)

        if len(candles_fetch) == 0:
            raise HTTPException(status_code=422, detail="Problem with binance api")

    except ConnectionError:
        raise HTTPException(status_code=500, detail="Server error")

    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=400, detail="Please enter valid symbol")

    score_short_term = get_trend(candles_fetch, window=6)
    score_long_term = get_trend(candles_fetch)

    return {"short_term": score_short_term, "long_term": score_long_term}