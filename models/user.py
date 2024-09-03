#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.user_group import user_group_association
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

    # Define one to many relationship
    payouts = relationship('Payout', back_populates='user',
                           cascade='all, delete-orphan')
    contributions = relationship('Contribution', back_populates='user',
                                 cascade='all, delete-orphan')

    def to_dict(self, depth=1):
        """Convert the instance to a dictionary format."""

        # Define the level of serialization needed
        if depth <= 0:
            # Stop serialization when depth is zero or negative
            return {}

        dict_representation = super().to_dict(depth)
        # Handle 'users' relationship explicitly
        dict_representation['groups'] = [
            group.to_dict(depth - 1) for group in self.groups]
        dict_representation['payouts'] = [
            payout.to_dict(depth - 1) for payout in self.payouts]
        dict_representation['contributions'] = [
            contribution.to_dict(depth - 1) for contribution in self.contributions]

        return dict_representation
