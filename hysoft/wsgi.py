#!/usr/bin/env python

"""
WSGI config for hysoft project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import requests
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hysoft.settings")
# pylint: disable=invalid-name
application = DjangoWhiteNoise(get_wsgi_application())
