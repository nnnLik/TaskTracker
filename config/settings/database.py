from . import const

DATABASES = {
    "default": {
        "ENGINE": const.DB_ENGINE,
        "NAME": const.DB_NAME,
        "USER": const.DB_USER,
        "PASSWORD": const.DB_PASSWORD,
        "HOST": const.DB_HOST,
        "PORT": const.DB_PORT,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": const.REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": 450,
    }
}
