#!/usr/bin/python3
import unittest
from models.user import User
from models.group import Group
from models.round import Round
from models.payout import Payout
from models.base_model import BaseModel
"""
Module defines a test for the `Payout` class
"""


class TestPayout(unittest.TestCase):
    """
    Test Payout class
    """

    def setUp(self):
        """ Setup test environment """
        self.user = User(email="testuser@email.com", password="tst_pwd",
                         first_name="john", last_name="Doe")
        self.group = Group(name="group 1",
                           description="Help friends in crisis",
                           creator_id=user.id)
        self.round = Round(group_id=group.id, round_number=2, amount="5000")
        self.payout = Payout(round_id=self.round.id, group_id=self.group.id,
                             user_id=self.user.id, amount=5000)

    def test_class_attributes(self):
        """ Test class attributes """
        self.assertEqual(self.payout.user_id, self.user.id)
        self.assertEqual(self.payout.group_id, self.group.id)
        self.assertEqual(self.payout.round_id, self.round.id)
        self.assertEqual(self.payout.amount, 5000)

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.payout.user_id, int)
        self.assertIsInstance(self.payout.group_id, int)
        self.assertIsInstance(self.payout.round_id, int)
        self.assertIsInstance(self.payout.amount, int)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.payout, BaseModel)
