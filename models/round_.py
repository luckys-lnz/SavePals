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

    # Relationship back to the Group model
    group = relationship('Group', back_populates='rounds')

    # Define one to many relationship
    payouts = relationship('Payout', back_populates='round_',
                           cascade='all, delete-orphan')
    contributions = relationship('Contribution', back_populates='round_',
                                 cascade='all, delete-orphan')

    def to_dict(self, depth=1):
        """Convert the instance to a dictionary format."""
        dict_representation = super().to_dict(depth)

        # Define the level of serialization needed
        if depth <= 0:
            # Stop serialization when depth is zero or negative
            return {}
        # Handle 'payouts' and 'contributions' relationship explicitly
        dict_representation['payouts'] = [
            payout.to_dict(depth - 1) for payout in self.payouts]
        dict_representation['contributions'] = [
            cont.to_dict(depth - 1) for cont in self.contributions]

        return dict_representation
