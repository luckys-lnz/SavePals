#!/usr/bin/python3
import unittest
from models import storage
from models.user import User
from models.group import Group
from models.round_ import Round
from models.base_model import BaseModel
"""
Module defines a test for the `Round` class
"""


class TestRound(unittest.TestCase):
    """
    Test Round class
    """
    @classmethod
    def setUpClass(cls):
        """ Setup for all tests """
        cls.storage = storage

    def setUp(self):
        """ Setup test environment """
        self.storage._DBStorage__session.begin_nested()  # nested transaction
        user = User(email="testuser@email.com", password="tst_pwd",
                    first_name="john", last_name="Doe", user_name="ttoe")
        self.storage.new(user)
        self.storage.save()

        self.group = Group(name="group 1",
                           description="Help friends in crisis",
                           creator_id=user.id)
        self.storage.new(self.group)
        self.storage.save()

        self.round = Round(group_id=self.group.id, round_number=2, amount=5000)
        self.storage.new(self.round)
        self.storage.save()

    def tearDown(self):
        """ Clean up test environment """
        self.storage._DBStorage__session.rollback()  # Rollback transaction
        self.storage._DBStorage__session.remove()

    @classmethod
    def tearDownClass(cls):
        """ Cleanup after all tests """
        cls.storage.close()  # Use the close method to clean up resources

    def test_class_attributes(self):
        """ Test class attributes """
        self.assertEqual(self.round.group_id, self.group.id)
        self.assertEqual(self.round.round_number, 2)
        self.assertEqual(self.round.amount, 5000)

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.round.group_id, str)
        self.assertIsInstance(self.round.round_number, int)
        self.assertIsInstance(self.round.amount, int)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.round, BaseModel)
