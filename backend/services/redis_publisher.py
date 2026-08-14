"""
Author : Sofian Hussein
Date : 09.08.2026
Project : CryptoBot
Desc : Publish market data to Redis for inter-service communication
Help :
    Source: Claude (Anthropic) - claude.ai
    Prompt: Explain how to publish JSON-serialized candle data to a
             Redis pub/sub channel using the redis Python client,
             so a separate C++ service can subscribe and consume it.
"""
import json
import redis

redis_conn = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True)


def publish(candles, symbol):
    redis_conn.publish(f"candles:{symbol}", json.dumps(candles))
