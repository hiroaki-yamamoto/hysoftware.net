#!/usr/bin/env python
# coding=utf-8

"""Contact form."""

from flask.ext.wtf import Form, RecaptchaField
import wtforms.fields as fld
import wtforms.validators as vld


class ContactForm(Form):
    """Contact Form."""

    name = fld.StringField(
        "Your Name", validators=[vld.InputRequired()],
        render_kw={
            "class": "form-control",
            "data-ng-model": "contact.name",
            "data-ng-disabled": "contactForm.$submitted",
            "required": True
        }
    )
    company_name = fld.StringField(
        "Your Company Name", validators=[vld.Optional()],
        render_kw={
            "class": "form-control",
            "data-ng-model": "contact.company",
            "data-ng-disabled": "contactForm.$submitted"
        }
    )
    email = fld.StringField(
        "Email", validators=[vld.Email(), vld.InputRequired()],
        render_kw={
            "class": "form-control",
            "data-ng-model": "contact.email",
            "data-ng-disabled": "contactForm.$submitted",
            "required": True
        }
    )
    message = fld.TextAreaField(
        "Message", validators=[vld.InputRequired()],
        render_kw={
            "class": "form-control",
            "data-ng-model": "contact.message",
            "data-ng-disabled": "contactForm.$submitted",
            "required": True
        }
    )
    recaptcha = RecaptchaField(
        "I am not a bot", render_kw={
            "data-ng-model": "contact.recaptcha",
            "data-ng-disabled": "contactForm.$submitted",
            "required": True
        }
    )
