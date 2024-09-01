#!/usr/bin/python3
import unittest
from models import storage
from models.user import User
from models.group import Group
from models.round_ import Round
from models.contribution import Contribution
from models.base_model import BaseModel
"""
Module defines a test for the `Contribution` class
"""


class TestContribution(unittest.TestCase):
    """
    Test Contribution class
    """
    @classmethod
    def setUpClass(cls):
        """ Setup for all tests """
        cls.storage = storage

    def setUp(self):
        """ Setup test environment """
        self.storage._DBStorage__session.begin_nested()  # nested transaction
        self.user = User(email="testuser@email.com", password="tst_pwd",
                         first_name="john", last_name="Doe", user_name="lucky")
        self.storage.new(self.user)
        self.storage.save()

        self.group = Group(name="group 1",
                           description="Help friends in crisis",
                           creator_id=self.user.id)
        self.storage.new(self.group)
        self.storage.save()

        self.round = Round(group_id=self.group.id, round_number=2, amount=5000)
        self.storage.new(self.round)
        self.storage.save()
        self.contribution = Contribution(round_id=self.round.id,
                                         group_id=self.group.id,
                                         user_id=self.user.id,
                                         amount=5000.45)
        self.storage.new(self.contribution)
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
        self.assertEqual(self.contribution.user_id, self.user.id)
        self.assertEqual(self.contribution.group_id, self.group.id)
        self.assertEqual(self.contribution.round_id, self.round.id)
        self.assertEqual(self.contribution.amount, 5000.45)

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.contribution.user_id, str)
        self.assertIsInstance(self.contribution.group_id, str)
        self.assertIsInstance(self.contribution.round_id, str)
        self.assertIsInstance(self.contribution.amount, float)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.contribution, BaseModel)
