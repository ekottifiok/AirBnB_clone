#!/usr/bin/python3
# class BaseModel that defines all common
# attributes/methods for other classes
import datetime
import uuid


class BaseModel:
    def __init__(self, name=None, my_number=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today().isoformat()
        self.updated_at = datetime.datetime.today().isoformat()
        self.name = (None if name is None else name)
        self.my_number = (None if name is None else my_number)

    def __str__(self):
        return "[{}], ({}), <{}>".format(self.__class__.__name__, self.id, self.to_dict())

    def save(self, *args, **kwargs):

        self.updated_at = datetime.date

    def to_dict(self):
        dict_class = {"id": self.id, "created_at": self.created_at, "updated_at": self.updated_at}
        if self.name is not None:
            dict_class["name"] = self.name
        if self.my_number is not None:
            dict_class["my_number"] = self.my_number
        return dict_class
