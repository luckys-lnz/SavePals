#!/usr/bin/python3
"""python package"""

from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/api/v1')

from api.v1.auth.index import *
