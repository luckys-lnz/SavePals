#!/usr/bin/python3
import time
import unittest
from datetime import datetime
from models import storage
from models.user import User
from models.base_model import BaseModel
"""
Module defines a test for the `User` class
"""


class TestUser(unittest.TestCase):
    """
    Test User class
    """
    @classmethod
    def setUpClass(cls):
        """ Setup for all tests """
        cls.storage = storage

    def setUp(self):
        """ Setup test environment """
        self.storage._DBStorage__session.begin_nested()  # nested transaction
        self.user = User(email="testuser@email.com", password="tst_pwd",
                         first_name="john", user_name="ttes", last_name="Doe")
        self.storage.new(self.user)
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
        self.assertEqual(self.user.email, "testuser@email.com")
        self.assertEqual(self.user.password, "tst_pwd")
        self.assertEqual(self.user.first_name, "john")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.user_name, "ttes")

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.user_name, str)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.user, BaseModel)
