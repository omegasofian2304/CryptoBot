#include "redis_client.h"
#include <hiredis/hiredis.h>
#include <iostream>

redisContext* connect_redis() {
    redisContext* c = redisConnect("127.0.0.1", 6379);

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

std::pair<std::string, std::string> subscribe_and_listen(redisContext* c, std::string channel) {
    std::string subscribe_channel = "PSUBSCRIBE " + channel;
    redisReply* reply = (redisReply*)redisCommand(c, subscribe_channel.c_str());
    freeReplyObject(reply);


    while (true) {
        redisReply* message;
        if (redisGetReply(c, (void**)&message) != REDIS_OK) {
            eturn std::make_pair("", "");
        }

        // pub/sub messages are 3-element arrays: ["message", channel, content]
        if (message->type == REDIS_REPLY_ARRAY && message->elements == 4) {
            std::string exact_channel = message->element[2]->str;
            std::string content = message->element[3]->str;
            freeReplyObject(message);
            return std::make_pair(exact_channel, content);
        }

        freeReplyObject(message);
    }
}

void publish_trend(redisContext* c, std::string symbol, double score) {
    std::string message = std::to_string(score);

    std::string channel = "trend:" + symbol;

    redisReply* reply = (redisReply*)redisCommand(
        c, "PUBLISH %s %s", channel.c_str(), message.c_str()
    );

    freeReplyObject(reply);
}