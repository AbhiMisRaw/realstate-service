import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = "localhost"
DB_PORT = 3308
DB_NAME = os.getenv("DB_NAME")

ALGORITHM = os.getenv("ALGORITHM","HS256")
ACCESS_TOKEN_EXP_MIN = os.getenv("ACCESS_TOKEN_EXP_MIN")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
