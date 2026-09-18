"""
Author : Sofian Hussein
Date : 11.08.2026
Project : CryptoBot
Desc : Subscribe to the c++
"""
import redis
import json

redis_conn = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True)

def subscribe_setup(symbol):
    pubsub = redis_conn.pubsub()
    pubsub.subscribe(f"trend:{symbol}")
    return pubsub


def wait_for_trend(pubsub):
    for message in pubsub.listen():
        if message["type"] == "message":
            return json.loads(message["data"])
