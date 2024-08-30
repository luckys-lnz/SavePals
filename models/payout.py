#!/usr/bin/python3
"""
Module defines Payout class
"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey


class Payout(BaseModel, Base):
    """Representation of the payouts table."""
    __tablename__ = 'payouts'

    # table colums
    round_id = Column(String, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    amount = Column(Float, nullable=False)
