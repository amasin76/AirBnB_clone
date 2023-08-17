#!/usr/bin/python3
"""Unittest test_state module"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for TestState class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_state(self):
        """Test the State class"""
        my_state = State()
        my_state.name = "Tanger-Tetouan-Al Hoceima"
        my_state.save()

        all_objs = self.storage.all()
        key = f'State.{my_state.id}'
        self.assertIn(key, all_objs.keys())

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.state
        self.assertIsNotNone(models.state.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(State.__doc__)
