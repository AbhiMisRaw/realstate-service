import json
from typing import Optional

import redis.asyncio as redis
from app.constants import ACCESS_TOKEN_EXP_MIN

class RedisClient:
    client: Optional[redis.Redis] = None

redis_client = RedisClient()

def get_redis():
    return redis_client.client


class RedisWrapper():
    client = get_redis()

    @staticmethod
    async def save_user(email: str, user_info: dict):
        client = get_redis()
        if client is None:
            raise RuntimeError("Redis is not initialized")
        
        # Convert dict to JSON string
        value = json.dumps(user_info)
        return await client.set(
            email,
            value,
            ex=int(ACCESS_TOKEN_EXP_MIN)*60
        )

    @staticmethod
    async def get_user(email: str):
        client = get_redis()

        if client is None:
            raise RuntimeError("Redis is not initialized")
        
        data = await client.get(email)
        if data:
            try:
                return json.loads(data)
            except:
                return None
        return None