#!/usr/bin/python3
import unittest
from models.user import User
from models.group import Group
from models.round import Round
from models.contribution import Contribution
from models.base_model import BaseModel
"""
Module defines a test for the `Contribution` class
"""


class TestContribution(unittest.TestCase):
    """
    Test Contribution class
    """

    def setUp(self):
        """ Setup test environment """
        self.user = User(email="testuser@email.com", password="tst_pwd",
                         first_name="john", last_name="Doe")
        self.group = Group(name="group 1",
                           description="Help friends in crisis",
                           creator_id=user.id)
        self.round = Round(group_id=group.id, round_number=2, amount="5000")
        self.contribution = Contribution(round_id=self.round.id,
                                         group_id=self.group.id,
                                         user_id=self.user.id,
                                         amount=5000)

    def test_class_attributes(self):
        """ Test class attributes """
        self.assertEqual(self.contribution.user_id, self.user.id)
        self.assertEqual(self.contribution.group_id, self.group.id)
        self.assertEqual(self.contribution.round_id, self.round.id)
        self.assertEqual(self.contribution.amount, 5000)

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.contribution.user_id, int)
        self.assertIsInstance(self.contribution.group_id, int)
        self.assertIsInstance(self.contribution.round_id, int)
        self.assertIsInstance(self.contributions.amount, int)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.contribution, BaseModel)
