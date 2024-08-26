#!/usr/bin/python3
"""
This module defines a Group class
"""
from models.base_model import BaseModel, Base
from models.use_group import user_group_association
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Group(BaseModel, Base):
    """This class defines a group by various attributes"""

    __tablename__ = 'groups'
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    creator_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    users = relationship('User',
                         secondary=user_group_association,
                         back_populates='groups')
