#!/usr/bin/env python
# coding=utf-8

"""Configuration for development."""

from datetime import timedelta
import os
from cbsettings import DjangoDefaults


class DevelConfig(DjangoDefaults):
    """Config for devleopment."""

    BASE_DIR = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ))
    ISSUE_BOARD = "https://github.com/hysoftware/hysoftware.net/issues"
    ISSUE_TXT = ""
    SECRET_KEY = 'si0%k#galmbd0vzpp817e!1v*a=lu!!$b&3b4l8$^4-3!-aj!s'
    DEBUG = True
    ALLOWED_HOSTS = ('localhost', '127.0.0.1')
    TITLE = "hysoft"
    SOURCE_URL = "https://github.com/hysoftware/hysoftware.net"

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_otp.DjangoOTP',
        'django_countries',
        'captcha',
        "app.common.apps.CommonConfig",
        "app.home.apps.HomeConfig",
        "app.user.apps.UserConfig",
        "app.legal.apps.LegalConfig"
    )

    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
    )

    ROOT_URLCONF = 'app.urls'

    TEMPLATES = (
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': [os.path.join(BASE_DIR, "app", "jinja2")],
            'APP_DIRS': True,
            'OPTIONS': {"environment": "app.jinja_env.jinja_options"}
        },
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    )

    WSGI_APPLICATION = 'app.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'devel.db',
        }
    }

    AUTHENTICATION_BACKENDS = ("django_otp.backends.OTPAuthBackend", )

    AUTH_PASSWORD_VALIDATORS = (
        {
            "NAME": ("django.contrib.auth.password_validation.%s") % cls_name
        } for cls_name in [
            "UserAttributeSimilarityValidator",
            "MinimumLengthValidator",
            "CommonPasswordValidator",
            "NumericPasswordValidator"
        ]
    )

    PASSWORD_HASHERS = (
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher"
    )

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATIC_URL = '/static/'
    STATIC_ROOT = \
        os.environ.get("STATIC_ROOT") or os.path.join(
            BASE_DIR, "staticfiles"
        )
    MEDIA_ROOT = \
        os.environ.get("MEDIA_ROOT") or os.path.join(
            BASE_DIR, "uploads"
        )
    MEDIA_URL = "/uploads/"
    CELERY_BROKER_URL = "redis://"
    CELERY_RESULT_BACKEND = "redis://"
    CELERY_RESULT_SERIALIZER = "msgpack"
    CELERY_ACCEPT_CONTENT = ("msgpack", )
    CELERY_TASK_SERIALIZER = "msgpack"
    CELERY_BEAT_SCHEDULE = {
        "refresh_github_profile": {
            "task": "user.github.fetch",
            "schedule": timedelta(hours=12)
        }
    }
    MAILGUN_KEY = "key-c0c09ef43a4d3a146d3945828fec775c"
    MAILGUN_URL = (
        "https://api.mailgun.net/v3/"
        "sandboxfb18aceb2a7948219de7080947534455.mailgun.org"
    )
    DEFAULT_FROM_EMAIL = "no-reply@hysoftware.net"

    RECAPTCHA_PUBLIC_KEY = "6Lc2dSETAAAAAI-VoBJQwjoCS88gmoNhXpcT-Pht"
    RECAPTCHA_PRIVATE_KEY = "6Lc2dSETAAAAAEl0AHy6OmYZhY7qifnE_04G9az4"
    NOCAPTCHA = True
