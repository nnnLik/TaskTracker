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
        "LOCATION": const.REDIS_CACHE_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": 450,
    }
}

CELERY_BROKER_URL = const.REDIS_BROKER_LOCATION
CELERY_RESULT_BACKEND = const.REDIS_BROKER_LOCATION
CELERY_ACCEPT_CONTENT = [
    "application/json",
]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Etc/UTC"
CELERY_ENABLE_UTC = True