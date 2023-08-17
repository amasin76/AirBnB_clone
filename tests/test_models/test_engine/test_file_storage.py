#!/usr/bin/python3
"""Unittest test_file_storage module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import pycodestyle


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""

    def setUp(self):
        """Set up test cases"""
        self.file_path = 'file.json'
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after test cases"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """Test the new method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        key = f"BaseModel.{my_model.id}"
        all_objs = self.storage.all()
        self.assertIn(key, all_objs.keys())
        self.assertEqual(all_objs[key], my_model)

    def test_save(self):
        """Test the save method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            content = f.read()
            key = f"BaseModel.{my_model.id}"
            self.assertIn(key, content)

    def test_reload(self):
        """Test the reload method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, all_objs.keys())

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        import models.engine.file_storage
        self.assertIsNotNone(models.engine.file_storage.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all_docstring(self):
        """Test that the all method has a docstring"""
        self.assertIsNotNone(FileStorage.all.__doc__)

    def test_new_docstring(self):
        """Test that the new method has a docstring"""
        self.assertIsNotNone(FileStorage.new.__doc__)

    def test_save_docstring(self):
        """Test that the save method has a docstring"""
        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_reload_docstring(self):
        """Test that the reload method has a docstring"""
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
