#!/usr/bin/python3
"""
FileStorage module
"""
from json import dump, load
from os import path
from models.base_model import BaseModel


class FileStorage:
    """
    the storage class to store an instance of any model
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return all the objects saved in the file
        :return: dict
        """
        return self.__objects

    def new(self, obj):
        """
        Add new objects to the self dictionary
        """
        # self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj
        pass

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as file_write:
            dump({key: value.to_dict() for key, value in self.__objects.items()}, file_write)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file_read:
                data_read = load(file_read)
                for _, value in data_read.items():
                    base_name = value.pop('__class__')
                    self.new(eval(base_name)(**value))
