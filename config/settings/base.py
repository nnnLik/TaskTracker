from pathlib import Path

from . import const

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = const.SECRET_KEY

DEBUG = const.DEBUG

ALLOWED_HOSTS = const.ALLOWED_HOSTS


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "rest_framework",
    "djoser",
    "corsheaders",
    "django_filters",
    "drf_yasg",
    "src.todo",
    "src.core",
    "src.tasks",
    "src.notification",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
]


ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Etc/UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static/"

MEDIA_URL = "/images/"
MEDIA_ROOT = BASE_DIR / "images/"

VIDEO_URL = "/videos/"
VIDEO_ROOT = BASE_DIR / "videos/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
