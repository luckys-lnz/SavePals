#!/usr/bin/python3
import time
import unittest
from datetime import datetime
from models.user import User
from models.group import Group
from models.base_model import BaseModel
"""
Module defines a test for the `Group` class
"""


class TestGroup(unittest.TestCase):
    """
    Test Group class
    """

    def setUp(self):
        """ Setup test environment """
        self.user = User(email="testuser@email.com", password="tst_pwd",
                         first_name="john", last_name="Doe")
        self.group = Group(name="group 1",
                           description="Help friends in crisis",
                           creator_id=self.user.id)

    def test_class_attributes(self):
        """ Test class attributes """
        self.assertEqual(self.group.name, "group 1")
        self.assertEqual(self.group.description, "Help friends in crisis")
        self.assertEqual(self.group.creator_id, self.user.id)

    def test_class_attributes_type(self):
        """ Test class attributes type """
        self.assertIsInstance(self.group.name, str)
        self.assertIsInstance(self.group.description, str)
        self.assertIsInstance(self.group.creator_id, str)

    def test_inherits_from_base_model(self):
        """ Test class inherits from `BaseModel` class """
        self.assertIsInstance(self.user, BaseModel)

    def test_user_group_relationship(self):
        """ Test many-to-many relationship between User and Group """
        group1 = Group(name="Group 1")
        group2 = Group(name="Group 2")
        self.user.groups.append(group1)
        self.user.groups.append(group2)

        self.assertIn(group1, self.user.groups)
        self.assertIn(group2, self.user.groups)
        self.assertIn(self.user, group1.users)
        self.assertIn(self.user, group2.users)
