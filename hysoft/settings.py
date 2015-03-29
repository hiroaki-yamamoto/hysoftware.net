"""
Django settings for hysoft project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("mode") != "production"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None

if DEBUG:
    SECRET_KEY = ("").join(
        [
            random.choice(
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEVGHIJKLMNOPQRSTUVWXYZ"
                "0123456789"
                "`~!@#$%^&*()-_=+[{]}\\|\"';:/?.>,<"
            )
        ]
    )
else:
    SECRET_KEY = os.environ["SECRET"]

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'about',
    'contact',
    'home'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dj_ajax_redirect.middleware.AjaxRedirectionMiddleware'
)

DISABLE_REDIRECT = [
    r"^manager"
]

ROOT_URLCONF = 'hysoft.urls'

WSGI_APPLICATION = 'hysoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': ('django.db.backends.sqlite3'
                   if DEBUG else
                   'django.db.backends.postgresql_psycopg2'),
        'NAME': (os.path.join(BASE_DIR, 'hysoft.db')
                 if DEBUG else "hysoft"),
        'USER': os.environ.get("db_user"),
        'PASSWORD': os.environ.get("db_pw"),
        'HOST': '127.0.0.1'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get("STATIC_ROOT", None)

# Session settings
SESSION_COOKIE_SECURE = False
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Email settings
EMAIL_BACKEND = None

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CONTACT_VIRIFICATION_EXPIRES = timedelta(hours=2)
