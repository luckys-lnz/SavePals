#!/usr/bin/python3

"""
Round table holds data for next collector in a group.

Base on the plan agreement.
"""

import models
from models.engine import DBstorage
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Payout(BaseModel, Base):
    """Representation of the user turns table."""

    if models.storage_t == 'db':
        __tablename__ = 'payout'

        #table colums
        id = Column(Integer, primary_key=True)
        round_id = Column(Integer, ForeignKey=('round.id'), nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        amount = Column(Float, nullable=False)
        payment_date = Column(sqlalchemy.DateTime, nullable=False,
                              default=sqlalchemy.funct.now())

        # Table Relationships
        round = relationship('Round', back_populates='payouts')
        user = relationship('User', back_populates='payouts')

    else:
        round_id = 0
        user_id = 0
        amount = 0.00
        payment_date = None

