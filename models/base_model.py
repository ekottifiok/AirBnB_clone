#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
"""

import datetime
import uuid


class BaseModel:
    """
    The base model of the class
    """
    def __init__(self, *args, **kwargs):
        """
        initializes an instance of the class
        :param args: won’t be used
        :param kwargs: is not empty will be used to
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs != {}:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        handles the print of the class
        :return: string
        """
        return "[{}], ({}), <{}>".format(self.__class__.__name__, self.id, self.to_dict())

    def save(self):
        """
        handles the save call of the instance
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self) -> dict:
        """
        converts the instance of the class to a dictionary
        :return: a dictionary
        """
        result_dict = {}
        for key in self.__dict__:
            value = self.__getattribute__(key)
            if value.__class__.__name__ == 'datetime':
                value = value.isoformat()
            result_dict[key] = value
        return {**result_dict, **{"__class__": self.__class__.__name__}}
