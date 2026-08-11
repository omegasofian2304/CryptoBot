#pragma once

#include <string>
#include <hiredis/hiredis.h>
#include <nlohmann/json.hpp>

redisContext* connect_redis();
void psubscribe(redisContext* c, std::string pattern);
std::pair<std::string, std::string> listen_next(redisContext* c);
void publish_trend(redisContext* c, std::string symbol, nlohmann::json score);
