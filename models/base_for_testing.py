#!/usr/bin/python3
"""This module defines a TestBase class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class TestBase(BaseModel, Base):
    """This class defines a Base table by various attributes"""
    __tablename__ = 'testbase'
    name = Column(String(128), nullable=False)
