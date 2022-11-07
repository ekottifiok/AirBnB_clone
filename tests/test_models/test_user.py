#!/usr/bin/python3
"""
User test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.user import User
from models import storage


class TestUser_instantiation(TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        self.assertNotEqual(User().id, User().id)

    def test_two_users_different_created_at(self):
        self.assertLess(User().created_at, User().created_at)

    def test_two_users_different_updated_at(self):
        self.assertLess(User().updated_at, User().updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        self.assertIn("[User] (123456)", us.__str__())
        self.assertIn("'id': '123456'", us.__str__())
        self.assertIn("'created_at': " + dt_repr, us.__str__())
        self.assertIn("'updated_at': " + dt_repr, us.__str__())

    def test_args_unused(self):
        self.assertNotIn(None, User(None).__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSaving(TestCase):
    """
    Unittest for the class User
    """



    def test_save(self):
        """
        unittest for the save method of the Amenity class
        :return:
        """
        _user = User()
        _user.updated_at = datetime(2018, 2, 28, 2, 6, 55, 258896)
        date_stored = _user.updated_at
        _user.save()
        self.assertNotEqual(date_stored, _user.updated_at)

    def test_to_dict(self):
        """
        Unittest for the to_dict method of the Amenity class
        :return:
        """
        _user = User()
        self.assertDictEqual(_user.to_dict(), {
            'id': _user.id,
            'created_at': _user.created_at.isoformat(),
            'updated_at': _user.updated_at.isoformat(),
            '__class__': _user.__class__.__name__
        })

    def test_public_attr(self):
        """
        Unittest for the public attributes for the User class
        :return:
        """
        _user = User()
        _user.email = "trial_email"
        self.assertEqual(_user.email, 'trial_email')
        _user.password = "trial_password"
        self.assertEqual(_user.password, 'trial_password')
        _user.first_name = "trial_first_name"
        self.assertEqual(_user.first_name, 'trial_first_name')
        _user.last_name = "trial_last_name"
        self.assertEqual(_user.last_name, 'trial_last_name')


if __name__ == "__main__":
    main()
