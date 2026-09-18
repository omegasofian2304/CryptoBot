#include "redis_client.h"
#include <hiredis/hiredis.h>
#include <iostream>
#include <nlohmann/json.hpp>

redisContext* connect_redis() {
    redisContext* c = redisConnect("redis", 6379);

    if (c == nullptr || c->err) {
        if (c) {
            std::cout << "Connection error : " << c->errstr << std::endl;
        }
        else {
            std::cout << "Unable to allocate Redis context" << std::endl;
        }
        return nullptr;
    }

    return c;
}

void psubscribe(redisContext* c, std::string pattern) {
    std::string cmd = "PSUBSCRIBE " + pattern;
    redisReply* reply = (redisReply*)redisCommand(c, cmd.c_str());
    if (reply) freeReplyObject(reply);
}

std::pair<std::string, std::string> listen_next(redisContext* c) {
    while (true) {
        redisReply* message;
        if (redisGetReply(c, (void**)&message) != REDIS_OK)
            return std::make_pair("", "");

        // pmessage = ["pmessage", pattern, channel, payload] -> 4 elements
        if (message->type == REDIS_REPLY_ARRAY && message->elements == 4) {
            std::string exact_channel = message->element[2]->str;
            std::string content = message->element[3]->str;
            freeReplyObject(message);
            return std::make_pair(exact_channel, content);
        }
        freeReplyObject(message);
    }
}

void publish_trend(redisContext* c, std::string symbol, nlohmann::json score) {
    std::string message = score.dump();
    std::string channel = "trend:" + symbol;

    redisReply* reply = (redisReply*)redisCommand(
        c, "PUBLISH %s %s", channel.c_str(), message.c_str());

    if (reply != nullptr) {
        freeReplyObject(reply);
    }
}