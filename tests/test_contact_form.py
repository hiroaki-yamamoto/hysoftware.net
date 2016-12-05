#!/usr/bin/env python
# coding=utf-8

"""ContactForm Tests."""

import uuid
from unittest.mock import patch, call, MagicMock
from django.contrib.auth import get_user_model
from django.test import TestCase

from app.user.forms import ContactForm
from app.user.models import UserInfo


class ContactFormTest(TestCase):
    """Contact form test when info_id is specified."""

    def setUp(self):
        """Setup."""
        self.info_id = uuid.uuid4()
        self.user = get_user_model().objects.create_user(
            username="test", password="test", email="test@example.com"
        )
        self.info = UserInfo.objects.create(
            id=self.info_id, user=self.user, github="octocat"
        )
        self.form = ContactForm({
            "user": str(self.info_id),
            "company_name": "Test Corp",
            "primary_name": "Test Name",
            "email": "test@example.com",
            "message": "This is a test",
            "g-recaptcha-response": "PASSED"
        })
        self.field = self.form.fields["user"]
        self.assertTrue(self.form.is_valid(), self.form.errors)

    def test_form(self):
        """The destination field should have inital value."""
        form = ContactForm(info_id=self.info_id)
        field = form.fields["user"]
        self.assertEqual(field.initial, self.info_id)

    @patch("app.user.forms.ctask")
    @patch("app.user.forms.loader")
    def test_save(self, loader, ctask):
        """Save function should send celery task asynchronously."""
        def get_template_side_effect(name):
            """Get template side effect."""
            def render_side_effect(*args, **kwargs):
                return "client_html" if name == "mail/client.html" \
                    else "client_txt" if name == "mail/client.txt" \
                    else "staff_html" if name == "mail/staff.html" \
                    else "staff_txt" if name == "mail/staff.txt" \
                    else None
            ret = MagicMock()
            ret.render.side_effect = render_side_effect
            return ret

        loader.get_template.side_effect = get_template_side_effect

        self.form.save()
        self.assertEqual(loader.get_template.call_count, 4)
        self.assertEqual(ctask.send_task.call_count, 2)
        loader.get_template.assert_has_calls([
            call("mail/client.html"),
            call("mail/client.txt"),
            call("mail/staff.html"),
            call("mail/staff.txt")
        ])
        ctask.send_task.assert_has_calls([
            call(
                "user.mail", (
                    self.form.instance.email,
                    "Thanks for your interest!",
                    "client_html", "client_txt"
                )
            ),
            call(
                "user.mail", (
                    self.info.user.email,
                    "Someone is interested in you through hysoftware.net",
                    "staff_html", "staff_txt"
                )
            )
        ])


class ContactFormWithoutEmailTest(TestCase):
    """Contact form test when info_id is specified."""

    def setUp(self):
        """Setup."""
        self.info_id = uuid.uuid4()
        self.user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        self.info = UserInfo.objects.create(
            id=self.info_id, user=self.user, github="octocat"
        )
        self.form = ContactForm({
            "user": str(self.info_id),
            "company_name": "Test Corp",
            "primary_name": "Test Name",
            "email": "test@example.com",
            "message": "This is a test",
            "g-recaptcha-response": "PASSED"
        })
        self.field = self.form.fields["user"]
        self.assertTrue(self.form.is_valid(), self.form.errors)

    @patch("app.user.forms.ctask")
    @patch("app.user.forms.loader")
    def test_save_without_staff_email(self, loader, ctask):
        """Save function should send celery task without staff email."""
        def get_template_side_effect(name):
            """Get template side effect."""
            def render_side_effect(*args, **kwargs):
                return "client_html" if name == "mail/client.html" \
                    else "client_txt" if name == "mail/client.txt" \
                    else None
            ret = MagicMock()
            ret.render.side_effect = render_side_effect
            return ret

        loader.get_template.side_effect = get_template_side_effect

        self.form.save()
        self.assertEqual(loader.get_template.call_count, 2)
        self.assertEqual(ctask.send_task.call_count, 1)
        loader.get_template.assert_has_calls([
            call("mail/client.html"),
            call("mail/client.txt")
        ])
        ctask.send_task.assert_called_once_with(
            "user.mail", (
                self.form.instance.email,
                "Thanks for your interest!",
                "client_html", "client_txt"
            )
        )
