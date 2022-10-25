#!/usr/bin/python3
from __future__ import annotations

import cmd


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to my simple console"
    prompt = "(hbnb) "
    file = None

    def do_help(self, arg: str) -> str:
        """handles the help command

        Args:
            arg (str): accepts keyword help

        Returns:
            str: the documented commands
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
