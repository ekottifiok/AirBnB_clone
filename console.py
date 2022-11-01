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
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

accepted_model = ['BaseModel', 'User', 'City',
                  'Place', 'Amenity', 'Review', 'State']


def parse_arg(arg: str, no_args=1) -> list[str] | None:
    if arg == '':
        print('** class name missing **')
        return None
    arg_array = arg.split()
    len_array = len(arg_array)
    if arg_array[0] not in accepted_model:
        print('** class doesn\'t exist **')
        return None
    if len_array < 2 and no_args >= 2:
        print('** instance id missing **')
        return None
    all_data_file = storage.all()
    if no_args > 1 and f"{arg_array[0]}.{arg_array[1]}"\
            not in all_data_file.keys():
        print('** no instance found **')
        return None
    return arg_array


class HBNBCommand(cmd.Cmd):
    """
    The class definition for the console
    """
    # intro = "Welcome to my simple console"
    prompt = "(hbnb) "
    _file_name = "file.json"

    def __init__(self):
        """
        initializes the instance class
        """
        self.__model_init = None
        self.__all_objects = storage.all()

        super().__init__()

    def emptyline(self) -> bool:
        """
        handles an emptyline
        :return: bool false
        """
        return False

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
        print("")
        return True

    def do_create(self, arg: str):
        """
        handles the create command
        :param arg: accepts keyword create
        :return:
        """
        arg_create = parse_arg(arg)
        len_array = len(arg_create)
        if arg_create is None:
            return False
        if len_array != 1:
            return False
        print(eval(arg_create[0])().id)
        storage.save()

    def do_show(self, arg: str):
        """
        handles the show command
        :param arg: accepts keyword show
        :return:
        """
        arg_show = parse_arg(arg, 2)
        if arg_show is None:
            return False
        object_id = f'{arg_show[0]}.{arg_show[1]}'
        print(storage.all().get(object_id))

    def do_destroy(self, arg: str):
        """
        handles the destroy command
        :param arg: accepts keyword destroy
        :return:
        """
        arg_show = parse_arg(arg, 2)
        if arg_show is None:
            return False
        del storage.all()[f'{arg_show[0]}.{arg_show[1]}']
        storage.save()

    def do_all(self, arg: str):
        """
        handles the all command
        :param arg: accepts keyword all
        :return:
        """
        arg_all = None
        result = []
        if arg != '':
            arg_all = parse_arg(arg)
            if arg_all is None:
                return False
        for key, value in storage.all().items():
            if arg_all is not None and arg_all[0] not in key:
                continue
            result.append(value.__str__())
        print(result)

    def do_update(self, arg: str):
        """
        handles the update command
        :param arg: accepts keyword update
        :return:
        """
        arg_update = parse_arg(arg, 3)
        if arg_update is None:
            return False
        arg_len = len(arg_update)
        if arg_len < 3:
            print("** attribute name missing **")
            return
        attr_name = arg_update[2]
        class_object = storage.all().get(f'{arg_update[0]}.{arg_update[1]}')
        if attr_name not in class_object.__dict__.keys():
            print('** value missing **')
            return
        if attr_name in ['id', 'created_at', 'updated_at']:
            return
        if arg_len < 4:
            arg_update.append('')
        class_object.__setattr__(attr_name, arg_update[3])
        storage.save()

    def do_User(self, arg: str):
        """
        handles all commands for the User
        :param arg: accepts keyword User
        :return:
        """
        if arg == '':
            return
        arg_array = arg[1:-1].split('(')
        command = arg_array[0]
        if command not in HBNBCommand._instance_command:
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
            arg_array[1] = arg_array[1][1:-1] \
                .replace('{', '').replace('}', '') \
                .replace(':', '').replace(',', '') \
                .replace('\'', '').replace('"', '')
            new_arg_array = arg_array[1].split(' ')
            len_new_arg_array = len(new_arg_array)
            if len_new_arg_array < 3 or len_new_arg_array % 2 != 1:
                return
            for key in range(1, len_new_arg_array, 2):
                update_str = ' '.join([
                    'User', new_arg_array[0],
                    new_arg_array[key], new_arg_array[key + 1]])
                self.do_update(update_str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
