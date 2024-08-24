#!/usr/bin/python3
import time
import unittest
from datetime import datetime
from models.user import User
"""
Module defines a test for the `User` class
"""


class TestUser(unittest.TestCase):
    """
    Test User class
    """

    def setUp(self):
        """ Setup test environment """
        self.user = User()

    def test_class_attributes(self):
        """ Test class attributes """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.user_name, "")

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.user, BaseModel)
