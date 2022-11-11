#!/usr/bin/python3
"""
Place test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.place import Place


class test_Place(TestCase):
    """
    Unittest for the class Place
    """

    def test_init(self):
        """
        unittest for the instantiation of the Amenity
        :return: None
        """
        _place = Place()
        self.assertIsNotNone(_place)
        self.assertIsNotNone(_place, Place)
        self.assertTrue(hasattr(_place, 'id'))
        self.assertTrue(hasattr(_place, 'created_at'))
        self.assertTrue(hasattr(_place, 'updated_at'))
        self.assertTrue(hasattr(_place, 'name'))
        _place_dict = _place.to_dict()

        # testing *args and **kwargs
        new_place = Place(**_place_dict)
        self.assertIsNotNone(new_place)
        self.assertIsInstance(new_place, Place)
        self.assertTrue(hasattr(new_place, 'id'))
        self.assertTrue(hasattr(new_place, 'created_at'))
        self.assertTrue(hasattr(new_place, 'updated_at'))

    def test_save(self):
        """
        unittest for the save method of the Amenity class
        :return:
        """
        _place = Place()
        _place.updated_at = datetime(2018, 2, 28, 2, 6, 55, 258896)
        date_stored = _place.updated_at
        _place.save()
        self.assertNotEqual(date_stored, _place.updated_at)

    def test_to_dict(self):
        """
        Unittest for the to_dict method of the Amenity class
        :return:
        """
        _place = Place()
        self.assertDictEqual(_place.to_dict(), {
            'id': _place.id,
            'created_at': _place.created_at.isoformat(),
            'updated_at': _place.updated_at.isoformat(),
            '__class__': _place.__class__.__name__
        })

    def test_public_attr(self):
        """

        :return:
        """
        _place = Place()
        _place.name = "trial_name"
        self.assertEqual(_place.name, 'trial_name')


if __name__ == "__main__":
    main()
