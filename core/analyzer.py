"""
Author : Sofian Hussein
Date : 23.03.2026
Project : Bitcoin trading Backend
Desc : Analyze the market
"""
from services.binance_api import get_candles


def get_trend():
    """
    Trend detection based on Dow Theory (Higher Highs / Higher Lows)
    Source: https://www.investopedia.com/terms/t/trendanalysis.asp
    """
    candles = get_candles("BTCUSDT", "1h", 100)



