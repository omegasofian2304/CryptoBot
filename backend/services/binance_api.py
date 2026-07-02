"""
Author : Sofian Hussein
Date : 23.03.2026
Project : Bitcoin trading Backend
Desc : API data fetching script
"""
import requests


def get_candles(symbol, interval, limit):
    """
    Fetch candlestick data from Binance API

    Args:
        symbol (str): Trading pair ex: BTCUSDT
        interval (str): Candle interval ex: 1h, 4h, 1d
        limit (int): Number of candles to fetch (max 1000)

    Returns:
        List of dictionaries containing OHLCV candle data
        Each candle: { open, high, low, close, volume }

    Example:
        get_candles("BTCUSDT", "1h", 100)
    """
    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    candles = []

    for data in response.json():
        candle = {
            "open": float(data[1]),
            "high": float(data[2]),
            "low": float(data[3]),
            "close": float(data[4]),
            "volume": float(data[5])
        }
        candles.append(candle)

    return candles

