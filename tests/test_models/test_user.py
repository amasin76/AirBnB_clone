#!/usr/bin/python3
"""Unittest test_user module"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for TestUser class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_user(self):
        """Test the User class"""
        my_user = User()
        my_user.first_name = "Khaled"
        my_user.last_name = "Ibn Al-Walid"
        my_user.email = "unbeatable@leader.war"
        my_user.password = "TheSwordOfGod"
        my_user.save()

        all_objs = self.storage.all()
        key = f'User.{my_user.id}'
        self.assertIn(key, all_objs.keys())

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.user
        self.assertIsNotNone(models.user.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(User.__doc__)
