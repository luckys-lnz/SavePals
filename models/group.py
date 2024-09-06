#!/usr/bin/python3
"""
This module defines a Group class
"""
from models.base_model import BaseModel, Base
from models.user_group import user_group_association
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Group(BaseModel, Base):
    """This class defines a group by various attributes"""

    __tablename__ = 'groups'
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    creator_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Define many to many relationships
    users = relationship('User',
                         secondary=user_group_association,
                         back_populates='groups')

    # Define one to many relationships
    rounds = relationship('Round', back_populates='group',
                          cascade="all, delete-orphan")
    payouts = relationship('Payout', back_populates='group',
                           cascade='all, delete-orphan')
    contributions = relationship('Contribution', back_populates='group',
                                 cascade='all, delete-orphan')

    def to_dict(self, depth=1):
        """Convert the instance to a dictionary format."""

        # Define the level of serialization needed
        if depth <= 0:
            # Stop serialization when depth is zero or negative
            return {}

        dict_representation = super().to_dict(depth)
        # Handle 'users' relationship explicitly
        dict_representation['users'] = [user.to_dict(depth - 1) for user in self.users]
        dict_representation['rounds'] = [rnd.to_dict(depth - 1) for rnd in self.rounds]
        dict_representation['payouts'] = [
            payout.to_dict(depth - 1) for payout in self.payouts]
        dict_representation['contributions'] = [
            contribution.to_dict(depth - 1) for contribution in self.contributions]

        return dict_representation
