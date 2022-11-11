#!/usr/bin/python3
"""
Amenity test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.amenity import Amenity


class test_Amenity(TestCase):
    """
    Unittest for the class Amenity
    """

    def test_init(self):
        """
        unittest for the instantiation of the Amenity
        :return: None
        """
        _amenity = Amenity()
        self.assertTrue(hasattr(_amenity, 'id'))
        self.assertTrue(hasattr(_amenity, 'created_at'))
        self.assertTrue(hasattr(_amenity, 'updated_at'))
        self.assertTrue(hasattr(_amenity, 'name'))
        self.assertIsNotNone(_amenity)
        self.assertIsNotNone(_amenity, Amenity)
        _amenity_dict = _amenity.to_dict()

        # testing *args and **kwargs
        new_amenity = Amenity(**_amenity_dict)
        self.assertTrue(hasattr(new_amenity, 'id'))
        self.assertTrue(hasattr(new_amenity, 'created_at'))
        self.assertTrue(hasattr(new_amenity, 'updated_at'))
        self.assertIsNotNone(new_amenity)
        self.assertIsInstance(new_amenity, Amenity)

    def test_save(self):
        """
        unittest for the save method of the Amenity class
        :return:
        """
        user = Amenity()
        user.updated_at = datetime(2018, 2, 28, 2, 6, 55, 258896)
        date1 = user.updated_at
        user.save()
        self.assertNotEqual(date1, user.updated_at)

    def test_to_dict(self):
        """
        Unittest for the to_dict method of the Amenity class
        :return:
        """
        _amenity = Amenity()
        self.assertDictEqual(_amenity.to_dict(), {
            'id': _amenity.id,
            'created_at': _amenity.created_at.isoformat(),
            'updated_at': _amenity.updated_at.isoformat(),
            '__class__': _amenity.__class__.__name__
        })

    def test_public_attr(self):
        """

        :return:
        """
        _amenity = Amenity()
        _amenity.name = "trial_name"
        self.assertEqual(_amenity.name, 'trial_name')


if __name__ == "__main__":
    main()
