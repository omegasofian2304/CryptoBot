"""
Author : Sofian Hussein
Date : 23.03.2026
Project : CryptoBot
Desc : Analyze the market
Help :
    Source: Claude (Anthropic) - claude.ai
    Prompt: Explain mathematically and progressively the EMA concept,
             from basic intuition to EMA(t) = Price(t) * k + EMA(t-1) * (1-k),
             including why k = 2/(N+1) and how to choose N for smoothing
             price data before detecting Dow Theory pivots.
"""
from backend.services.binance_api import get_candles

def calculate_ema(prices, n):
    k = 2 / (n+1)
    ema = [prices[0]]
    for i in range(1, len(prices)):
        ema_value = prices[i] * k + ema[i-1] * (1-k)
        ema.append(ema_value)
    return ema


def get_swings(candles_dow,field):
    value = []
    swing_value = []

    # sorted by value
    for candle in candles_dow:
        value.append(candle[field])

    # sorted by ema value
    ema_value = calculate_ema(value, 20)

    sign = 1 if field == "high" else -1
    adjusted = [v * sign for v in ema_value]

    for i in range(1, len(adjusted) - 1):
        if adjusted[i] > adjusted[i-1] and adjusted[i] > adjusted[i+1]:
            swing_value.append(ema_value[i])

    return swing_value

def check_score(score_dow):
    if score_dow >= 0.6:
        return "haussier"
    elif score_dow <= 0.4:
        return "baissier"
    else:
        return "instable"


def trend_score(points):
    if len(points) < 2:
        return 0
    up = sum(1 for i in range(1, len(points)) if points[i] > points[i-1])
    total = len(points) - 1
    return up / total


def get_trend(candles_dow, window=None):
    highs = get_swings(candles_dow, field="high")
    lows = get_swings(candles_dow, field="low")

    if window:
        highs = highs[-window:]
        lows = lows[-window:]

    highs_score = trend_score(highs)
    lows_score = trend_score(lows)
    return (highs_score + lows_score) / 2

def test():
    candles = get_candles("BTCUSDT", "1h", 1000)

    score_long_term = get_trend(candles)
    score_short_term = get_trend(candles, window=6)

    print("Long term :", check_score(score_long_term), "Score : ", score_long_term)
    print("Short term :", check_score(score_short_term), "Score : ", score_short_term)
