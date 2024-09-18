#!/usr/bin/python3
import time
import unittest
from datetime import datetime
from models import storage
from models.base_for_testing import TestBase
"""
Module defines a test for the `BaseModel` class
"""


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel class
    """
    @classmethod
    def setUpClass(cls):
        """ Setup for all tests """
        cls.storage = storage

    def setUp(self):
        """ SetUp test environment """
        self.storage._DBStorage__session.begin_nested()  # nested transaction
        self.obj = TestBase(name="test 1")
        self.storage.new(self.obj)
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
        """ tests instance attributes """
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_str_method(self):
        """tests __str__ method"""
        obj_str = "[{}] ({}) {}".format(
                  type(self.obj).__name__, self.obj.id, self.obj.__dict__)
        self.assertEqual(str(self.obj), obj_str)

    def test_save_method(self):
        """tests save method"""
        prev_time = self.obj.updated_at

        # delay execution of next line of code
        time.sleep(1)

        # update the object
        self.obj.save()

        curr_time = self.obj.updated_at

        self.assertNotEqual(curr_time, prev_time)

    def test_to_dict_method(self):
        """tests to_dict method"""

        # create a dict
        obj_dict = self.obj.to_dict()
        cls_name = obj_dict.get('__class__')

        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(cls_name, 'TestBase')

        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_kwargs_passed(self):
        """tests for object created from dictionary"""

        # create the dict
        obj_dict = self.obj.to_dict()

        # create object
        new_obj = TestBase(**obj_dict)

        self.assertNotIn('__class__', new_obj.__dict__)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)
