#!/usr/bin/python3
import time
import unittest
from datetime import datetime
from models.base_model import BaseModel
"""
Module defines a test for the `Group` class
"""


class TestUser(unittest.TestCase):
    """
    Test Group class
    """

    def setUp(self):
        """ Setup test environment """
        self.group = Group()

    def test_class_attributes(self):
        """ Test class attributes """
        self.assertEqual(self.group.name, "")
        self.assertEqual(self.group.description, "")
        self.assertEqual(self.group.creator_id, "")

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.group.name, str)
        self.assertIsInstance(self.group.description, str)
        self.assertIsInstance(self.group.creator_id, str)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.user, BaseModel)
