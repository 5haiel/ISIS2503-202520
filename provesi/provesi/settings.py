
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-do-not-use-in-prod")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = [h for h in os.getenv("ALLOWED_HOSTS", "*").split(",") if h]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

CSRF_TRUSTED_ORIGINS = [o for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if o]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users", "locations", "producto", "catalog", "inventory", "orders",
    "shipping", "payment", "experiment", "wms_op",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "provesi.experiment.diagnostics.CacheDiagnosticsMiddleware",  # opcional
]

ROOT_URLCONF = "provesi.provesi.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ],
    },
}]

WSGI_APPLICATION = "provesi.provesi.wsgi.application"

USE_SQLITE = os.getenv("USE_SQLITE", "false").lower() == "true"

if USE_SQLITE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "monitoring_db"),
            "USER": os.getenv("DB_USER", "monitoring_user"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "5432"),
            "CONN_MAX_AGE": int(os.getenv("DB_CONN_MAX_AGE", "60")),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "en-us")
TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# primary key
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# cache redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{os.getenv('CACHE_HOST','localhost')}:{os.getenv('CACHE_PORT','6379')}/0",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "TIMEOUT": int(os.getenv("CACHE_TTL", str(60 * 5))),  # 5 min por defecto
    }
}

CACHE_DEFAULT_TTL = int(os.getenv("CACHE_DEFAULT_TTL", str(60 * 5)))
CACHE_SHORT_TTL   = int(os.getenv("CACHE_SHORT_TTL",   "60"))
CACHE_LONG_TTL    = int(os.getenv("CACHE_LONG_TTL",    str(60 * 60 * 24)))

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": int(os.getenv("DRF_PAGE_SIZE", "50")),
}

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": LOG_LEVEL},
}
