#!/usr/bin/env python
# coding=utf-8

"""Setting test."""

import re
from unittest.mock import patch

from django.test import TestCase


class ProductionConfigTest(TestCase):
    """Production Configuration Test."""

    def setUp(self):
        """Setup."""
        self.environ = {
            "SECRET": "test",
            "RECAPTCHA_PUBLIC_KEY": "recaptcha_test_pubkey",
            "RECAPTCHA_PRIVATE_KEY": "recaptcha_test_privkey",
            "MAILGUN_KEY": "mailgun-key",
            "MAILGUN_URL": "mailgun-url",
            "ALLOWED_HOSTS": (
                "allowed.io, allowed2.io,allowed3.io, allowed4.io,"
            ),
            "CELERY_BROKER_URL": "test_broker",
            "DB_ENGINE": "test_db_engine",
            "DB_NAME": "test_db_name",
            "DB_USER": "test_db_user",
            "DB_PW": "test_db_pw",
            "DB_HOST": "test_db_host",
            "DB_PORT": "test_db_port"
        }
        self.sep = re.compile(",\\s.")
        with patch.dict("os.environ", self.environ):
            from app.settings.public import PublicConfig
            self.conf_p = PublicConfig
        from app.settings.devel import DevelConfig
        self.conf_d = DevelConfig

    def test_subclass(self):
        """Production config should be a subclass of DevelConfig."""
        self.assertTrue(issubclass(self.conf_p, self.conf_d))

    def test_secret(self):
        """Secret key should be proper."""
        self.assertNotEqual(self.conf_p.SECRET_KEY, self.conf_d.SECRET_KEY)
        self.assertEqual(self.conf_p.SECRET_KEY, self.environ["SECRET"])

    def test_recaptcha(self):
        """Recaptcha secret and public should be proper."""
        self.assertNotEqual(
            self.conf_p.RECAPTCHA_PUBLIC_KEY,
            self.conf_d.RECAPTCHA_PUBLIC_KEY
        )
        self.assertEqual(
            self.conf_p.RECAPTCHA_PUBLIC_KEY,
            self.environ["RECAPTCHA_PUBLIC_KEY"]
        )
        self.assertNotEqual(
            self.conf_p.RECAPTCHA_PRIVATE_KEY,
            self.conf_d.RECAPTCHA_PRIVATE_KEY
        )
        self.assertEqual(
            self.conf_p.RECAPTCHA_PRIVATE_KEY,
            self.environ["RECAPTCHA_PRIVATE_KEY"]
        )

    def test_mailgun(self):
        """Mailgun test."""
        self.assertNotEqual(self.conf_p.MAILGUN_KEY, self.conf_d.MAILGUN_KEY)
        self.assertNotEqual(self.conf_p.MAILGUN_URL, self.conf_d.MAILGUN_URL)
        self.assertEqual(self.conf_p.MAILGUN_KEY, self.environ["MAILGUN_KEY"])
        self.assertEqual(self.conf_p.MAILGUN_URL, self.environ["MAILGUN_URL"])

    def test_allowed_hosts(self):
        """Allowed host test."""
        self.assertNotEqual(
            self.conf_p.ALLOWED_HOSTS,
            self.conf_d.ALLOWED_HOSTS
        )
        self.assertEqual(
            self.conf_p.ALLOWED_HOSTS,
            self.sep.split(self.environ["ALLOWED_HOSTS"])
        )

    def test_celery_broker(self):
        """Celery broker should be differ from devel env."""
        self.assertNotEqual(
            self.conf_p.CELERY_BROKER_URL,
            self.conf_d.CELERY_BROKER_URL
        )
        self.assertEqual(
            self.conf_p.CELERY_BROKER_URL,
            self.environ["CELERY_BROKER_URL"]
        )

    def test_db(self):
        """Database URL should be differ from devel."""
        # "DB_ENGINE": "test_db_engine",
        # "DB_NAME": "test_db_name",
        # "DB_PW": "test_db_pw",
        # "DB_HOST": "test_db_host",
        # "DB_PORT": "test_db_port"
        self.assertNotEqual(self.conf_p.DATABASES, self.conf_d.DATABASES)
        self.assertDictEqual({
            "default": {
                "ENGINE": self.environ["DB_ENGINE"],
                "NAME": self.environ["DB_NAME"],
                "USER": self.environ["DB_USER"],
                "PASSWORD": self.environ["DB_PW"],
                "HOST": self.environ["DB_HOST"],
                "PORT": self.environ["DB_PORT"]
            }
        }, self.conf_p.DATABASES)
