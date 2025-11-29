from fastapi import FastAPI
from fastapi.requests import Request
import redis.asyncio as redis

from app.redis import redis_client
from app.routes import user_routes, property_routes
from app.utils.db import init_models


app = FastAPI(
    on_startup=[init_models]
)


@app.get("/ping")
async def ping(request: Request):
    return {"ping":"pong"}

app.include_router(user_routes)
app.include_router(property_routes)


@app.on_event("startup")
async def startup():
    print("Connecting to Redis...")
    redis_client.client = redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True
    )
    print("Connection Successfull...")


@app.on_event("shutdown")
async def shutdown():
    if redis_client.client:
        await redis_client.client.close()
