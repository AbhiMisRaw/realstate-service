#!/bin/bash

# Custom MySQL Container for FastAPI Project

CONTAINER_NAME="fastapi_mysql"
MYSQL_ROOT_PASSWORD="rootpass"
DB_USER="appuser"
DB_PASSWORD="apppassword"
DB_NAME="fastapi_db"

# Remove old container if exists
docker rm -f $CONTAINER_NAME 2>/dev/null

# Start MySQL container
docker run -d \
  --name $CONTAINER_NAME \
  -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
  -e MYSQL_USER=$DB_USER \
  -e MYSQL_PASSWORD=$DB_PASSWORD \
  -e MYSQL_DATABASE=$DB_NAME \
  -p 3308:3306 \
  mysql:8.0

echo "[+] MySQL container started."
echo "    Host: localhost"
echo "    Port: 3306"
echo "    DB Name: $DB_NAME"
echo "    DB User: $DB_USER"
echo "    DB Password: $DB_PASSWORD"
