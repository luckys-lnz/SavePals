#!/usr/bin/python3
"""python package"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.dashboard import *
from api.v1.views.round_ import *
from api.v1.views.transaction import *
from api.v1.views.user import *
from api.v1.views.group import *
