#!/usr/bin/python3
''' unit test module for filestorage class'''
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)

class test_storage(unittest.TestCase):
    '''file storage class definition'''

    def setUp(self):
        """ check empty """
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ check remove class """
        try:
            remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        """ check empty class  """
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """ check  all function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_save_create(self):
        """ Save  """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id

        self.assertEqual(obj, storage.all()[obj_key])

    def test_new_empty(self):
        '''check new method'''
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_class(self):
        '''check new method is valid'''
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        
        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        self.assertEqual(obj, storage.all()[obj_key])

    def test_reload(self):
        '''check reload classes'''
        obj - BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)

if __name__ == "__main__":
    unittest.main()
