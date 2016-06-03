#!/usr/bin/env python
# coding=utf-8

"""Contact controller."""

from bson import ObjectId
from flask import make_response, jsonify, current_app, render_template
from flask.ext.classy import FlaskView
from .forms import ContactForm
from ..user.models import Person


class ContactView(FlaskView):
    """Contact controller."""

    trailing_slash = False

    def post(self):
        """POST request."""
        mail = current_app.extensions["mail"]
        form = ContactForm()
        if not form.validate():
            return make_response(jsonify(form.errors), 417)
        person = Person.objects(id=ObjectId(form.to.data)).get()
        mail.send_message(
            subject="Mail sending service from hysoftware.net",
            sender=form.email.data, body=form.message.data,
            recipients=[person.email]
        )
        mail.send_message(
            subject="Thanks for your interest!",
            sender="noreply@hysoftware.net",
            recipients=[form.email.data],
            body=render_template(
                "mail_to_client.txt", form=form, member=person.fullname
            )
        )
        return ""
