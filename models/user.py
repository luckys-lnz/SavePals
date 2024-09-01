#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.use_group import user_group_association
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    user_name = Column(String(128), nullable=False)

    # Relationship to Group through the association table
    groups = relationship('Group',
                          secondary=user_group_association,
                          back_populates='users')
