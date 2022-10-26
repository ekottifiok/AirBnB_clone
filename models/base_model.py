#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    the base model of the class
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an instance of the class
        :param args: won’t be used
        :param kwargs: is not empty will be used to
        """
        if kwargs:
            for key, value in kwargs.items():
                if key is "__class__":
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """
        handles the print of the class
        :return: string
        """
        return "[{:s}], ({:s}), <{:s}>".format(self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """
        handles the save call of the instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        converts the instance of the class to a dictionary
        :return: a dictionary
        """
        return {**self.__dict__.copy(), **{
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }}
