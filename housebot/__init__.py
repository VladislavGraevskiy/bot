# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

import os
from flask import Flask
from .database import db


def create_app():
    app = Flask(__name__)
    # app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import housebot.housemodule.controllers as housem

    app.register_blueprint(housem.module)

    return app