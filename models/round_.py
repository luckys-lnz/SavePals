#!/usr/bin/python3
"""
This module defines a Round class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Round(BaseModel, Base):
    """This class defines a round by various attributes"""

    __tablename__ = 'rounds'
    round_number = Column(String(128), nullable=False)
    amount = Column(String(128), nullable=False)
    group_id = Column(String(60), ForeignKey('groups.id'),
                      nullable=False)
