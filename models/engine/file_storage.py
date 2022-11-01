#!/usr/bin/python3
"""
FileStorage module
"""
from json import dump, load
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    """
    the storage class to store an instance of any model
    """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """
        Return all the objects saved in the file
        :return: dict
        """
        return self.__objects

    def new(self, obj):
        """
        Add new objects to the self dictionary
        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """
        saves new files to self.__file_path
        :return:
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as f_write:
            dump({key: value.to_dict()
                  for key, value in self.__objects.items()}, f_write)

    def reload(self):
        """
        retrieves data from a file self.__file_path
        :return:
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f_read:
                data_read = load(f_read)
                for _, value in data_read.items():
                    self.new(eval(value.pop('__class__'))(**value))
