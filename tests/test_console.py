#!/usr/bin/python3
"""
Defines unittests for console.py
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
from unittest import TestCase
from console import HBNBCommand
from io import StringIO
from unittest import mock, TestCase, main


class TestHBNBCommand_prompt(TestCase):
    """
    Defines unittest for the prompt
        - test_prompt_string()
        - test_empty_line()
    """

    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        self.assertFalse(HBNBCommand().onecmd(""))
        self.assertEqual("", self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_help(TestCase):
    """
    Defines test for the help
        - test_help()
        - test_help_help()
        - test_EOF()
        - test_create()
        - test_show()
        - test_destroy()
        - test_all()
        - test_update()
        - test_show()
    """

    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_help(self):
        help_result = ("Documented commands (type help <topic>):\n"
                       "========================================\n"
                       "EOF  User  all  create  destroy  help  quit "
			" show  update")
        self.assertFalse(HBNBCommand().onecmd("help"))
        self.assertEqual(help_result, self.patcher.getvalue().strip())

    def test_help_help(self):
        help_help_result = """handles the help command
        :param arg: accepts keyword help
        :return: the documented commands"""
        self.assertFalse(HBNBCommand().onecmd("help help"))
        self.assertEqual(help_help_result, self.patcher.getvalue().strip())

    def test_EOF(self):
        EOF_result = """handles the EOF command which is
        :param arg: EOF is empty line + ENTER
        :return: bool True"""
        self.assertFalse(HBNBCommand().onecmd('help EOF'))
        self.assertEqual(EOF_result, self.patcher.getvalue().strip())

    def test_create(self):
        create_result = """handles the create command
        :param arg: accepts keyword create
        :return:"""
        self.assertFalse(HBNBCommand().onecmd('help create'))
        self.assertEqual(create_result, self.patcher.getvalue().strip())

    def test_show(self):
        show_result = """handles the show command
        :param arg: accepts keyword show
        :return:"""
        self.assertFalse(HBNBCommand().onecmd('help show'))
        self.assertEqual(show_result, self.patcher.getvalue().strip())

    def test_destroy(self):
        destroy_result = """handles the destroy command
        :param arg: accepts keyword destroy
        :return:"""
        self.assertFalse(HBNBCommand().onecmd('help destroy'))
        self.assertEqual(destroy_result, self.patcher.getvalue().strip())

    def test_all(self):
        all_result = """handles the all command
        :param arg: accepts keyword all
        :return:"""
        self.assertFalse(HBNBCommand().onecmd('help all'))
        self.assertEqual(all_result, self.patcher.getvalue().strip())

    def test_update(self):
        update_result = """handles the update command
        :param arg: accepts keyword update
        :return:"""
        self.assertFalse(HBNBCommand().onecmd('help update'))
        self.assertEqual(update_result, self.patcher.getvalue().strip())

    def test_User(self):
        User_result = """handles all commands for the User
        :param arg: accepts keyword User
        :return:"""
        self.assertFalse(HBNBCommand().onecmd('help User'))
        self.assertEqual(User_result, self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_exit(TestCase):
    """
    Defines unittests for tests exits
        - test_quit_exit()
        - test_EOF_exit()
    """
    def test_quit_exit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exit(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(TestCase):
    """
    Defines unittests for tests create
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_class_name_missing(self):
        self.assertFalse(HBNBCommand().onecmd("create"))
        self.assertEqual('** class name missing **', self.patcher.getvalue().strip())

    def test_class_does_not_exist(self):
        self.assertFalse(HBNBCommand().onecmd('create MyUser'))
        self.assertEqual('** class doesn\'t exist **', self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_show(TestCase):
    """
    Defines unittests for tests show
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_class_name_missing(self):
        self.assertFalse(HBNBCommand().onecmd("show"))
        self.assertEqual('** class name missing **', self.patcher.getvalue().strip())

    def test_class_does_not_exist(self):
        self.assertFalse(HBNBCommand().onecmd('show MyUser'))
        self.assertEqual('** class doesn\'t exist **', self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_destroy(TestCase):
    """
    Defines unittests for tests destroy
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_class_name_missing(self):
        self.assertFalse(HBNBCommand().onecmd("destroy"))
        self.assertEqual('** class name missing **', self.patcher.getvalue().strip())

    def test_class_does_not_exist(self):
        self.assertFalse(HBNBCommand().onecmd('destroy MyUser'))
        self.assertEqual('** class doesn\'t exist **', self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_all(TestCase):
    """
    Defines unittests for tests all
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_class_name_missing(self):
        self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertEqual('** class name missing **', self.patcher.getvalue().strip())

    def test_class_does_not_exist(self):
        self.assertFalse(HBNBCommand().onecmd('all MyUser'))
        self.assertEqual('** class doesn\'t exist **', self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_update(TestCase):
    """
    Defines unittests for tests update
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    def test_class_name_missing(self):
        self.assertFalse(HBNBCommand().onecmd("update"))
        self.assertEqual('** class name missing **', self.patcher.getvalue().strip())

    def test_class_does_not_exist(self):
        self.assertFalse(HBNBCommand().onecmd('update MyUser'))
        self.assertEqual('** class doesn\'t exist **', self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()


class TestHBNBCommand_User(TestCase):
    """
    Defines unittests for tests create
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()

    # def test_class_name_missing(self):
    #     self.assertFalse(HBNBCommand().onecmd(".all()"))
    #     self.assertEqual('** class name missing **', self.patcher.getvalue().strip())

    def tearDown(self) -> None:
        self.sys_out.stop()

if __name__ == '__main__':
    main()
