#!/usr/bin/python3
"""
This module defines a user_group table
"""
from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base_model import Base


# Association table for many-to-many relationship between User and Group
user_group_association = Table(
    'user_group',
    Base.metadata,
    Column('user_id', String(60), ForeignKey('users.id'),
           primary_key=True),
    Column('group_id', String(60), ForeignKey('groups.id'),
           primary_key=True),
    Column('is_admin', Boolean, nullable=False, default=False),
    Column('joined_at', DateTime, nullable=False,
           default=datetime.utcnow)
)
