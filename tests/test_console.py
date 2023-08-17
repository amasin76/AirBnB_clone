#!/usr/bin/python3
"""Unittest test_console module"""

import unittest
from unittest.mock import patch
from io import StringIO
import console
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """TestHBNBCommand class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.storage.reload()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases"""
        self.storage._FileStorage__objects = {}

    def test_module_docstring(self):
        """Test that the module has a docstring"""
        self.assertIsNotNone(console.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.__doc__)

    def test_quit_docstring(self):
        """Test that the quit method has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.do_quit.__doc__)

    def test_EOF_docstring(self):
        """Test that the EOF method has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.do_EOF.__doc__)

    def test_emptyline_docstring(self):
        """Test that the emptyline method has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.emptyline.__doc__)

    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('quit')
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('EOF')
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command(self):
        """Test the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('')
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_create_command(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('create')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('create MyModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('create BaseModel')
            output = f.getvalue().strip()
            all_objs = self.storage.all()
            key = f'BaseModel.{output}'
            self.assertIn(key, all_objs.keys())

    def test_show_command(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('show')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('show MyModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('show BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

        my_model = BaseModel()
        my_model.save()

        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'show BaseModel {my_model.id}'
            console.HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            expected_output = str(my_model)
            self.assertEqual(output, expected_output)

    def test_destroy_command(self):
        """Test the destroy command"""
        my_model = BaseModel()
        my_model.save()

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('destroy')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('destroy MyModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('destroy BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'destroy BaseModel {my_model.id}'
            console.HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertEqual(output, '')

        all_objs = self.storage.all()
        key = f'BaseModel.{my_model.id}'
        self.assertNotIn(key, all_objs.keys())

    def test_all_command(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('all')
            output = f.getvalue().strip()
            self.assertEqual(output, '[]')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('all MyModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

        my_model1 = BaseModel()
        my_model1.save()

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('all')
            output = f.getvalue().strip()
            expected_output = f'[\"{str(my_model1)}\"]'
            self.assertEqual(output, expected_output)

        my_model2 = BaseModel()
        my_model2.save()

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('all')
            output = f.getvalue().strip()
            expected_output1 = str(my_model1)
            expected_output2 = str(my_model2)
            self.assertIn(expected_output1, output)
            self.assertIn(expected_output2, output)

    def test_update_command(self):
        """Test the update command"""
        my_model = BaseModel()
        my_model.save()

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('update')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('update MyModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd(f'update BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'update BaseModel {my_model.id}'
            console.HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertEqual(output, '** attribute name missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'update BaseModel {my_model.id} name'
            console.HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertEqual(output, '** value missing **')

        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'update BaseModel {my_model.id} name "Khaled"'
            console.HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertEqual(output, '')

        all_objs = self.storage.all()
        key = f'BaseModel.{my_model.id}'
        updated_obj = all_objs[key]
        self.assertEqual(updated_obj.name, 'Khaled')
