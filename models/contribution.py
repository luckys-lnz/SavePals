#!/usr/bin/python
"""
Module defines a `Contribution` class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Contribution(BaseModel, Base):
    """Representation of the user Contribution table."""
    __tablename__ = 'contributions'

    # table column
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    round_id = Column(String, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)

    # Relationship back to the Group model
    group = relationship('Group', back_populates='contributions')

    # Relationship back to the User model
    user = relationship('User', back_populates='contributions')

    # Relationship back to the Round model
    round_ = relationship('Round', back_populates='contributions')
