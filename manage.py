# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

import os
from flask_script import Manager

from housebot import create_app

app = create_app()
# app.config.from_object(os.environ['APP_SETTINGS'])
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
