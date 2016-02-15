#!/usr/bin/env python
# coding=utf-8

import os

from app import app

if __name__ == '__main__':
    app.run(
        host=os.environ.get("host", None),
        port=os.environ.get("port", None),
        threaded=True
    )
