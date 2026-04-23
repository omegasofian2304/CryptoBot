"""
Author : Sofian Hussein
Date : 23.03.2026
Project : Bitcoin trading Backend
Desc : Analyze the market
"""
from services.binance_api import get_candles


def get_trend():
    """
        Source : Claude
        Prompt : explains mathematically how the Dow algorithm works
    """
    candles = get_candles("BTCUSDT", "1h", 300)
    highs = []
    lows = []

    swing_lows = []
    swing_highs = []

    # sorted by lows and highs
    for candle in candles:
        highs.append(candle["high"])
        lows.append(candle["low"])

    # detect the swing lows
    for i in range(1, len(lows) - 1):
        if lows[i] < lows[i-1] and lows[i] < lows[i+1]:
            swing_lows.append(lows[i])

    # detect the swing highs
    for i in range(1, len(highs) - 1):
        if highs[i] > highs[i-1] and highs[i] > highs[i+1]:
            swing_highs.append(highs[i])


    print(swing_lows)
    print(swing_highs)
    if len(swing_lows) < 2 or len(swing_highs) < 2:
        return "indéterminé"

    if swing_lows[-2] < swing_lows[-1] and swing_highs[-2] < swing_highs[-1]:
        return "haussier"
    elif swing_lows[-2] > swing_lows[-1] and swing_highs[-2] > swing_highs[-1]:
        return "baissier"
    else:
        return "instable"


print(get_trend())
