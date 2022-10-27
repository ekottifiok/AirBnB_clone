#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
from __future__ import annotations
import cmd
from json import dump
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    The class definition for the console
    """
    intro = "Welcome to my simple console"
    prompt = "(hbnb) "

    def __init__(self):
        self.__accepted_model = ['BaseModel', 'User', 'City',
                                 'Place', 'Amenity', 'Review', 'State']
        self.__instance_command = ['all', 'count', 'show', 'destroy', 'update']
        self.__model_init = None
        self.__all_objects = storage.all()
        self.__file_name = "file.json"
        super().__init__()

    def do_help(self, arg: str) -> bool | None:
        """
        handles the help command
        :param arg: accepts keyword help
        :return: the documented commands
        """
        return super().do_help(arg)

    @staticmethod
    def do_quit(arg: str) -> bool:
        """
        handles the quit command
        :param arg: accepts keyword quit
        :return: bool True
        """
        return True

    @staticmethod
    def do_EOF(arg: str) -> bool:
        """
        handles the EOF command which is
        :param arg: EOF is empty line + ENTER
        :return: bool True
        """
        print('\n')
        return True

    def do_create(self, arg: str):
        """
        handles the create command
        :param arg: accepts keyword create
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        if arg not in self.__accepted_model:
            print('** class doesn\'t exist **')
            return
        self.__model_init = eval(arg)()
        self.__all_objects[arg + '.' + str(self.__model_init.id)] =\
            self.__model_init.to_dict()
        print(self.__model_init.id)
        with open(self.__file_name, mode='w', encoding='utf-8') as f_write:
            dump({key: value.to_dict()
                  for key, value in self.__all_objects.items()}, f_write)

    def do_show(self, arg: str):
        """
        handles the show command
        :param arg: accepts keyword show
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        class_name = arg.split()[0]
        if class_name not in self.__accepted_model:
            print('** class doesn\'t exist **')
            return
        try:
            id_string = arg.split()[1]
        except IndexError:
            print('** instance id missing **')
            return
        search_id = class_name + '.' + id_string
        if search_id in self.__all_objects.keys():
            print(self.__all_objects.get(search_id))
        else:
            print('** no instance found **')

    def do_destroy(self, arg: str):
        """
        handles the destroy command
        :param arg: accepts keyword destroy
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        class_name = arg.split()[0]
        if class_name not in self.__accepted_model:
            print('** class doesn\'t exist **')
            return
        try:
            id_string = arg.split()[1]
        except IndexError:
            print('** instance id missing **')
            return
        search_id = class_name + '.' + id_string
        if search_id in self.__all_objects.keys():
            self.__all_objects.pop(search_id)
            with open(self.__file_name, mode='w', encoding='utf-8') as f_write:
                dump({key: value.to_dict()
                      for key, value in self.__all_objects.items()}, f_write)
        else:
            print('** no instance found **')
            return

    def do_all(self, arg: str):
        """
        handles the all command
        :param arg: accepts keyword all
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        if arg not in self.__accepted_model:
            print('** class doesn\'t exist **')
            return
        result = []
        for key, value in self.__all_objects.items():
            if arg in key:
                result.append(value.__str__())
        print(result)

    def do_update(self, arg: str):
        """
        handles the update command
        :param arg: accepts keyword update
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        arg_array = arg.split()
        arg_len = len(arg_array)
        class_name = arg_array[0]
        if class_name not in self.__accepted_model:
            print('** class doesn\'t exist **')
            return
        if arg_len < 2:
            print('** instance id missing **')
            return
        id_string = arg_array[1]
        search_id = class_name + '.' + id_string
        if search_id not in self.__all_objects.keys():
            print('** no instance found **')
            return
        class_object = self.__all_objects.get(search_id)
        if arg_len < 3:
            print("** attribute name missing **")
            return
        attr_name = arg_array[2]
        if attr_name not in class_object.__dict__.keys():
            print('** value missing **')
            return
        if attr_name in ['id', 'created_at', 'updated_at']:
            return
        if arg_len < 4:
            return
        class_object.__setattr__(attr_name, arg_array[3])
        with open(self.__file_name, mode='w', encoding='utf-8') as f_write:
            dump({key: value.to_dict()
                  for key, value in self.__all_objects.items()}, f_write)

    def do_User(self, arg: str):
        if arg == '':
            return
        arg_array = arg[1:-1].split('(')
        command = arg_array[0]
        if command not in self.__instance_command:
            return
        if command == 'all':
            self.do_all('User')
        elif command == 'count':
            counter = 0
            for key in self.__all_objects.keys():
                if 'User' in key:
                    counter += 1
            print(counter)
        elif command == 'show':
            if len(arg_array) != 2:
                return
            self.do_show('User ' + arg_array[1][1:-1])
        elif command == 'destroy':
            if len(arg_array) != 2:
                return
            self.do_destroy('User ' + arg_array[1][1:-1])
        elif command == 'update':
            if len(arg_array) != 2:
                return
            arg_array[1] = arg_array[1][1:-1]\
                .replace('{', '').replace('}', '')\
                .replace(':', '').replace(',', '')\
                .replace('\'', '').replace('"', '')
            new_arg_array = arg_array[1].split(' ')
            len_new_arg_array = len(new_arg_array)
            if len_new_arg_array < 3 or len_new_arg_array % 2 != 1:
                return
            for key in range(1, len_new_arg_array, 2):
                update_str = ' '.join([
                    'User', new_arg_array[0],
                    new_arg_array[key], new_arg_array[key+1]])
                self.do_update(update_str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
