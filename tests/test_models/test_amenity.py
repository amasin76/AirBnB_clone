#!/usr/bin/python3
"""Unittest test_amenity module"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for TestAmenity class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_amenity(self):
        """Test the Amenity class"""
        my_amenity = Amenity()
        my_amenity.name = "Wifi"
        my_amenity.save()

        all_objs = self.storage.all()
        key = f'Amenity.{my_amenity.id}'
        self.assertIn(key, all_objs.keys())

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.amenity
        self.assertIsNotNone(models.amenity.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(Amenity.__doc__)
