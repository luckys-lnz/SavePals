#!/usr/bin/python3
"""
Module defines a Round class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Payout(BaseModel, Base):
    """Representation of the user turns table."""
    __tablename__ = 'payouts'

    # table colums
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    round_id = Column(String, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
