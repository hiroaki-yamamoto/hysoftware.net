#!/usr/bin/env python
# coding=utf-8

"""Controller for font-face."""

from flask import render_template, make_response
from flask.ext.classy import FlaskView


class OpenSansView(FlaskView):
    """OpenSansView."""

    trailing_slash = False
    unicode_range = [
        "U+0460-052F", "U+20B4", "U+2DE0-2DFF", "U+A640-A69F",
        "U+0400-045F", "U+0490-0491", "U+04B0-04B1", "U+2116",
        "U+1F00-1FFF", "U+0370-03FF", "U+0102-0103", "U+1EA0-1EF1",
        "U+20AB", "U+0100-024F", "U+1E00-1EFF", "U+20A0-20AB",
        "U+20AD-20CF", "U+2C60-2C7F", "U+A720-A7FF", "U+0000-00FF",
        "U+0131", "U+0152-0153", "U+02C6", "U+02DA", "U+02DC",
        "U+2000-206F", "U+2074", "U+20AC", "U+2212", "U+2215",
        "U+E0FF", "U+EFFD", "U+F000"
    ]

    def index(self):
        """Index page."""
        resp = make_response(
            render_template("opensans.css", unicode_range=self.unicode_range)
        )
        resp.mimetype = "text/css"
        return resp
