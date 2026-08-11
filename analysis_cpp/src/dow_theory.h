#pragma once

#include <vector>
#include <string>
#include "candle.h"

std::vector<double> calculate_ema(std::vector<double> prices, int n);
std::vector<double> get_swings(std::vector<Candle> candles_dow, std::string field);
std::string check_score(double score_dow);
double trend_score(std::vector<double> points);
double get_trend(std::vector<Candle> candles_dow, int window = -1);