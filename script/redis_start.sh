#!/bin/bash

# Custom Redis Container for FastAPI Project

CONTAINER_NAME="fastapi_redis"

# Remove old container if exists
docker rm -f $CONTAINER_NAME 2>/dev/null

# Start Redis container
docker run -d \
  --name $CONTAINER_NAME \
  -p 6379:6379 \
  redis:7.2 \
  redis-server --appendonly yes

echo "[+] Redis container started."
echo "    Host: localhost"
echo "    Port: 6379"
