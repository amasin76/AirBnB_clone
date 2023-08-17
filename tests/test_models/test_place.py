#!/usr/bin/python3
"""Unittest test_place module"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for TestPlace class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_place(self):
        """Test the Place class"""
        my_place = Place()
        my_place.city_id = "0001"
        my_place.user_id = "0002"
        my_place.name = "My place"
        my_place.description = "A cozy place in the city"
        my_place.number_rooms = 2
        my_place.number_bathrooms = 1
        my_place.max_guest = 4
        my_place.price_by_night = 100
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        my_place.amenity_ids = ["0003", "0004"]
        my_place.save()

        all_objs = self.storage.all()
        key = f'Place.{my_place.id}'
        self.assertIn(key, all_objs.keys())

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.place
        self.assertIsNotNone(models.place.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(Place.__doc__)
