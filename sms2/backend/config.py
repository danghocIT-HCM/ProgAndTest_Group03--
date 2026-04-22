import os

DB_HOST     = os.getenv("DB_HOST", "db")   # QUAN TRỌNG
DB_PORT     = int(os.getenv("DB_PORT", 3306))
DB_USER     = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_NAME     = os.getenv("DB_NAME", "edums")

SECRET_KEY  = 'edums_jwt_secret_2024'
DEBUG       = True
PORT        = 5000