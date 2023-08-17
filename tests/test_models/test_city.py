#!/usr/bin/python3
"""Unittest test_city module"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for TestCity class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_city(self):
        """Test the City class"""
        my_city = City()
        my_city.state_id = "R"
        my_city.name = "Al Hoceima"
        my_city.save()

        all_objs = self.storage.all()
        key = f'City.{my_city.id}'
        self.assertIn(key, all_objs.keys())

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.city
        self.assertIsNotNone(models.city.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(City.__doc__)
