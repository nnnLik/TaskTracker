from decouple import config


SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [host for host in v.split(",") if host]
)
CORS_ORIGIN_WHITELIST = config(
    "CORS_ORIGIN_WHITELIST",
    cast=lambda v: [origin.strip() for origin in v.split(",") if origin],
)

DB_ENGINE = config("DB_ENGINE")
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")

POSTGRES_NAME = config("POSTGRES_NAME")
POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")

REDIS_LOCATION = config("REDIS_LOCATION")
