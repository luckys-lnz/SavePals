#!/usr/bin/python3
"""
This module instantiates an object of class DBStorage
"""
from models.base_model import Base
from models.user import User
from models.group import Group
from models.round import Round
from models.payout import Payout
from models.contribution import Contribution
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
