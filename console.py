#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
from __future__ import annotations
import cmd
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
    file = None

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

    @staticmethod
    def do_create(arg: str):
        """
        handles the create command
        :param arg: accepts keyword create
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        if arg not in ['BaseModel', ]:
            print('** class doesn\'t exist **')
            return

    @staticmethod
    def do_show(arg: str):
        """
        handles the show command
        :param arg: accepts keyword show
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        class_name = arg.split()[0]
        if class_name not in ['BaseModel', ]:
            print('** class doesn\'t exist **')
            return
        try:
            id_string = arg.split()[1]
        except IndexError:
            print('** instance id missing **')
            return
        if id_string is not 'found':
            print('** no instance found **')
            return

    @staticmethod
    def do_destroy(arg: str):
        """
        handles the destroy command
        :param arg: accepts keyword destroy
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        class_name = arg.split()[0]
        if class_name not in ['BaseModel', ]:
            print('** class doesn\'t exist **')
            return
        try:
            id_string = arg.split()[1]
        except IndexError:
            print('** instance id missing **')
            return
        if id_string is not 'found':
            print('** no instance found **')
            return

    @staticmethod
    def do_all(arg: str):
        """
        handles the all command
        :param arg: accepts keyword all
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        if arg not in ['BaseModel', ]:
            print('** class doesn\'t exist **')
            return

    @staticmethod
    def do_update(arg: str):
        """
        handles the update command
        :param arg: accepts keyword update
        :return:
        """
        if arg == '':
            print('** class name missing **')
            return
        arg_array = arg.split()
        arg_len = len(arg)
        class_name = arg_array[0]
        if class_name not in ['BaseModel', ]:
            print('** class doesn\'t exist **')
            return
        try:
            id_value = int(arg_array[1])
        except [IndexError, ValueError]:
            print('** instance id missing **')
            return
        if arg_len == 2:
            print("** attribute name missing **")
        for key in range(2, arg_len, 2):
            try:
                value_attr = arg[key+1]
            except IndexError:
                print("** value missing **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
