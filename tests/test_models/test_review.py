#!/usr/bin/python3
"""Unittest test_review module"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for TestReview class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_review(self):
        """Test the Review class"""
        my_review = Review()
        my_review.place_id = "0001"
        my_review.review_id = "0002"
        my_review.text = "Great place, had a wonderful time!"
        my_review.save()

        all_objs = self.storage.all()
        key = f'Review.{my_review.id}'
        self.assertIn(key, all_objs.keys())

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.review
        self.assertIsNotNone(models.review.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(Review.__doc__)
