#!/usr/bin/python3

"""
Round table holds data for next collector in a group.

Base on the plan agreement.
"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Payout(BaseModel, Base):
    """Representation of the user turns table."""
    __tablename__ = 'payout'

    #table colums
    round_id = Column(String, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)

