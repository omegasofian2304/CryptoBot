#include <nlohmann/json.hpp>
#include "dow_theory.h"
#include "redis_client.h"
#include <string>
#include <vector>


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
	redisContext* connection = connect_redis();
	auto result = subscribe_and_listen(connection, "candles:*");
	std::string channel = result.first; 
	std::string json_text = result.second;
	std::vector<Candle> candles = parse_string_to_candle(json_text);
	double score = get_trend(candles);
	std::string symbol = channel.substr(channel.find(":") + 1);
	publish_trend(connection, channel, score);
	return 0;
}