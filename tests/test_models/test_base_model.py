#!/usr/bin/python3
"""Unittest test_base_model module"""

from datetime import datetime
from models.base_model import BaseModel
import unittest
from time import sleep
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.base_model
        self.assertIsNotNone(models.base_model.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_init_docstring(self):
        """Test that the __init__ method has a docstring"""
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_str_docstring(self):
        """Test that the __str__ method has a docstring"""
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_save_docstring(self):
        """Test that the save method has a docstring"""
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_to_dict_docstring(self):
        """Test that the to_dict method has a docstring"""
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        """Test the __init__ method of the BaseModel class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}"\
            .format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_save_updates_updated_at(self):
        """Test that the save method updates the updated_at attribute"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        sleep(0.1)
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Self explain"""
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)

    def test_to_dict_contains_correct_values(self):
        """Self explain"""
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertEqual(my_dict["id"], my_model.id)
