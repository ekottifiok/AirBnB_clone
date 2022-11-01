#!/usr/bin/python3
"""
User test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.user import User


class test_User(TestCase):
    """
    Unittest for the class User
    """

    def test_init(self):
        """
        unittest for the instantiation of the Amenity
        :return: None
        """
        _user = User()
        self.assertIsNotNone(_user)
        self.assertIsNotNone(_user, User)
        self.assertTrue(hasattr(_user, 'id'))
        self.assertTrue(hasattr(_user, 'created_at'))
        self.assertTrue(hasattr(_user, 'updated_at'))
        _user_dict = _user.to_dict()

        # testing *args and **kwargs
        new_user = User(**_user_dict)
        self.assertIsNotNone(new_user)
        self.assertIsInstance(new_user, User)
        self.assertTrue(hasattr(new_user, 'id'))
        self.assertTrue(hasattr(new_user, 'created_at'))
        self.assertTrue(hasattr(new_user, 'updated_at'))

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
