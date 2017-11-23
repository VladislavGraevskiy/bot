# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

from flask import Blueprint


module = Blueprint('entity', __name__, url_prefix='/entity')


@module.route('/', methods=['GET'])
def index():
    return 'Work'
