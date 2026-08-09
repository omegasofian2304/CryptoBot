#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "candle.h"
#include "dow_theory.h"

std::vector<double> calculate_ema(std::vector<double> prices, int n) {
    double denominator = (n + 1);
    double k = 2 / denominator;
    double ema_value;
    std::vector<double> ema = { prices[0] };
    for (int i = 1; i < prices.size(); i++) {
        ema_value = prices[i] * k + ema[i - 1] * (1 - k);
        ema.push_back(ema_value);
    }
    return ema;
}

std::vector<double> get_swings(std::vector<Candle> candles_dow, std::string field) {
    std::vector<double> value;
    std::vector<double> swing_value;
    std::string low_string = "low";
    std::vector<double> adjusted;
    int sign = 1;

    if (field == low_string) {
        for (int i = 0; i < candles_dow.size(); i++) {
            value.push_back(candles_dow[i].low);
        }
        sign = -1;
    }

    else {
        for (int i = 0; i < candles_dow.size(); i++) {
            value.push_back(candles_dow[i].high);
        }
    }

    // N=20: EMA smoothing window, tuned for 1h candles. Adjust if the
    // candle timeframe changes.
    const std::vector<double> ema_value = calculate_ema(value, 20);
    for (double v : ema_value) {
        adjusted.push_back(v * sign);
    }

    for (int i = 1; i < (adjusted.size() - 1); i++) {
        if (adjusted[i] > adjusted[i - 1] && adjusted[i] > adjusted[i + 1]) {
            swing_value.push_back(ema_value[i]);
        }
    }
    return swing_value;
}

std::string check_score(double score_dow) {
    if (score_dow >= 0.6) {
        return "bullish";
    }
    else if (score_dow <= 0.4) {
        return "bearish";
    }
    else {
        return "unstable";
    }
}

double trend_score(std::vector<double> points) {
    const int total = points.size() - 1;
    double up = 0;

    if (total < 1) {
        return 0.5;
    }

    for (int i = 1; i < points.size(); i++) {
        if (points[i] > points[i - 1]) {
            up += 1;
        }
    }

    return up / total;
}

// window = -1 means "no window": use all available swing points
// (long term). A positive value restricts to the last N pivots
// (short term).
double get_trend(std::vector<Candle> candles_dow, int window) {
    std::vector<double> highs = get_swings(candles_dow, "high");
    std::vector<double> lows = get_swings(candles_dow, "low");

    if (window != -1) {
        // (int) cast avoids the unsigned arithmetic trap: size() is unsigned,
        // so size() - window can "wrap around" to a huge number if
        // window > size(). std::max guarantees a non-negative index.
        int start_highs = std::max(0, (int)highs.size() - window);
        int start_lows = std::max(0, (int)lows.size() - window);
        std::vector<double> highs_windowed(highs.begin() + start_highs, highs.end());
        std::vector<double> lows_windowed(lows.begin() + start_lows, lows.end());

        double high_score = trend_score(highs_windowed);
        double low_score = trend_score(lows_windowed);
        return (high_score + low_score) / 2;
    }
    else {
        double high_score = trend_score(highs);
        double low_score = trend_score(lows);
        return (high_score + low_score) / 2;
    }
}