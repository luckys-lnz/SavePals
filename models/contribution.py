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



    def to_dict(self, depth=1):
        """Convert the instance to a dictionary format."""

        # Define the level of serialization needed
        if depth <= 0:
            # Stop serialization when depth is zero or negative
            return {}

        dict_representation = super().to_dict(depth)
        # Handle 'users' relationship explicitly
        dict_representation['user'] = self.user.to_dict(depth - 1)
        dict_representation['round'] = self.round_.to_dict(depth - 1)
        dict_representation['group'] = self.group.to_dict(depth - 1)

        return dict_representation
