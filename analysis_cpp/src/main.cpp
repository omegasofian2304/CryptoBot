#include <nlohmann/json.hpp>
#include "dow_theory.h"
#include "redis_client.h"
#include <string>
#include <vector>
#include <iostream>


std::vector<Candle> parse_string_to_candle(std::string to_parse) {
	nlohmann::json data = nlohmann::json::parse(to_parse);
	std::vector<Candle> candles;

	for (auto& item : data) {
		Candle c;
		c.open = item["open"];
		c.high = item["high"];
		c.low = item["low"];
		c.close = item["close"];
		c.volume = item["volume"];
		candles.push_back(c);
	}

	return candles;
}

int main() {
    redisContext* sub_conn = connect_redis();
    redisContext* pub_conn = connect_redis();

    if (sub_conn == nullptr || pub_conn == nullptr) {
        return 1;
    }

    psubscribe(sub_conn, "candles:*");

    while (true) {
        auto result = listen_next(sub_conn);
        std::string channel = result.first;
        std::string json_text = result.second;

        std::vector<Candle> candles = parse_string_to_candle(json_text);

        nlohmann::json scores;
        scores["short_term"] = get_trend(candles, 6);
        scores["long_term"] = get_trend(candles);

        std::string symbol = channel.substr(channel.find(":") + 1);
        publish_trend(pub_conn, symbol, scores);
    }
}