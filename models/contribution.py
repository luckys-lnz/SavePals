#!/usr/bin/python3

"""
Round table holds data for next collector in a group.

Base on the plan agreement.
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Contribution(BaseModel, Base):
    """Representation of the user Contribution table."""
    __tablename__ = 'contributions'

    # table columns
    round_id = Column(String, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
