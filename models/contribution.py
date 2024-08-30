#!/usr/bin/python3
"""
Module defines a Contribution class
"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey, Table


class Contribution(BaseModel, Base):
    """Representation of the Contribution table."""
    __tablename__ = 'contributions'

    # table columns
    round_id = Column(String, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    amount = Column(Float, nullable=False)
