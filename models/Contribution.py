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


class Contribution(BaseModel, Base):
    """Representation of the user Contribution table."""

    if models.storage_t == 'db':
        __tablename__ = 'contribution'

        # table colums
        id = Column(Integer, primary_key=True)
        round_id = Column(Integer, ForeignKey=('round.id'), nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        amount = Column(Float, nullable=False)
        payment_date = Column(sqlalchemy.DateTime, nullable=False,
                              default=sqlalchemy.funct.now())

        # Table Relationships
        round = relationship('Round', back_populates='contributions')
        user = relationship('User', back_populates='contributions')

    else:
        round_id = 0
        user_id = 0
        amount = 0.00
        payment_date = None


def __repr__(self):
    return "<Contribution(id='%i', round_id='%i', amount='%i')>" % (
                              self.id, self.round_id, self.amount)
