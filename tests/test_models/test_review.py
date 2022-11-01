#!/usr/bin/python3
"""
Review test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.review import Review


class test_Review(TestCase):
    """
    Unittest for the class Review
    """

    def test_init(self):
        """
        unittest for the instantiation of the Amenity
        :return: None
        """
        _review = Review()
        self.assertIsNotNone(_review)
        self.assertIsNotNone(_review, Review)
        self.assertTrue(hasattr(_review, 'id'))
        self.assertTrue(hasattr(_review, 'created_at'))
        self.assertTrue(hasattr(_review, 'updated_at'))
        _review_dict = _review.to_dict()

        # testing *args and **kwargs
        new_review = Review(**_review_dict)
        self.assertIsNotNone(new_review)
        self.assertIsInstance(new_review, Review)
        self.assertTrue(hasattr(new_review, 'id'))
        self.assertTrue(hasattr(new_review, 'created_at'))
        self.assertTrue(hasattr(new_review, 'updated_at'))

    def test_save(self):
        """
        unittest for the save method of the Amenity class
        :return:
        """
        _review = Review()
        _review.updated_at = datetime(2018, 2, 28, 2, 6, 55, 258896)
        date_stored = _review.updated_at
        _review.save()
        self.assertNotEqual(date_stored, _review.updated_at)

    def test_to_dict(self):
        """
        Unittest for the to_dict method of the Amenity class
        :return:
        """
        _review = Review()
        self.assertDictEqual(_review.to_dict(), {
            'id': _review.id,
            'created_at': _review.created_at.isoformat(),
            'updated_at': _review.updated_at.isoformat(),
            '__class__': _review.__class__.__name__
        })

    def test_public_attr(self):
        """

        :return:
        """
        _review = Review()
        _review.place_id = "trial_place_id"
        self.assertEqual(_review.place_id, 'trial_place_id')
        _review.user_id = "trial_user_id"
        self.assertEqual(_review.user_id, 'trial_user_id')
        _review.text = "trial_text"
        self.assertEqual(_review.text, 'trial_text')


if __name__ == "__main__":
    main()
