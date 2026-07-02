"""
Author : Sofian Hussein
Date : 23.03.2026
Project : Bitcoin trading Backend
Desc : Analyze the market
Help :
    Source : Claude
    Prompt : explains mathematically how the Dow algorithm works
"""
from backend.services.binance_api import get_candles

candles = get_candles("BTCUSDT", "1h", 240)

def trend_score(points):
    if len(points) < 2:
        return 0
    up = sum(1 for i in range(1, len(points)) if points[i] > points[i-1])
    total = len(points) - 1
    return up / total


def get_swings_highs(candles_dow):
    highs = []
    swing_highs = []

    # sorted by lows and highs
    for candle in candles_dow:
        highs.append(candle["high"])


    # detect the swing highs
    for i in range(1, len(highs) - 1):
        if highs[i] > highs[i-1] and highs[i] > highs[i+1]:
            swing_highs.append(highs[i])

    return swing_highs


def get_swings_lows(candles_dow):
    lows = []

    swing_lows = []

    # sorted by lows and highs
    for candle in candles_dow:
        lows.append(candle["low"])

    # detect the swing lows
    for i in range(1, len(lows) - 1):
        if lows[i] < lows[i-1] and lows[i] < lows[i+1]:
            swing_lows.append(lows[i])

    return swing_lows

def check_score(score_dow):
    if score_dow >= 0.6:
        return "haussier"
    elif score_dow <= 0.4:
        return "baissier"
    else:
        return "instable"


highs_score = trend_score(get_swings_highs(candles)[-6:])
lows_score = trend_score(get_swings_lows(candles)[-6:])

score = (highs_score + lows_score) / 2

print(get_swings_highs(candles))
print(get_swings_lows(candles))
print(score)
print(check_score(score))