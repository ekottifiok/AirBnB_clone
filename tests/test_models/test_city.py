#!/usr/bin/python3
"""
City test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.city import City


class test_City(TestCase):
    """
    Unittest for the class City
    """
    
    def test_init(self):
        """
        unittest for the instantiation of the Amenity
        :return: None
        """
        _city = City()
        self.assertIsNotNone(_city)
        self.assertIsNotNone(_city, City)
        self.assertTrue(hasattr(_city, 'id'))
        self.assertTrue(hasattr(_city, 'created_at'))
        self.assertTrue(hasattr(_city, 'updated_at'))
        self.assertTrue(hasattr(_city, 'name'))
        _city_dict = _city.to_dict()

        # testing *args and **kwargs
        new_city = City(**_city_dict)
        self.assertIsNotNone(new_city)
        self.assertIsInstance(new_city, City)
        self.assertTrue(hasattr(new_city, 'id'))
        self.assertTrue(hasattr(new_city, 'created_at'))
        self.assertTrue(hasattr(new_city, 'updated_at'))

    def test_save(self):
        """
        unittest for the save method of the Amenity class
        :return:
        """
        _city = City()
        _city.updated_at = datetime(2018, 2, 28, 2, 6, 55, 258896)
        date_stored = _city.updated_at
        _city.save()
        self.assertNotEqual(date_stored, _city.updated_at)

    def test_to_dict(self):
        """
        Unittest for the to_dict method of the Amenity class
        :return:
        """
        _city = City()
        self.assertDictEqual(_city.to_dict(), {
            'id': _city.id,
            'created_at': _city.created_at.isoformat(),
            'updated_at': _city.updated_at.isoformat(),
            '__class__': _city.__class__.__name__
        })

    def test_public_attr(self):
        """

        :return:
        """
        _city = City()
        _city.name = "trial_name"
        self.assertEqual(_city.name, 'trial_name')


if __name__ == "__main__":
    main()
