#pragma once

#include <string>
#include <hiredis/hiredis.h>

redisContext* connect_redis();
std::pair<std::string, std::string> subscribe_and_listen(redisContext* c, std::string channel);
void publish_trend(redisContext* c, std::string symbol, double score);
