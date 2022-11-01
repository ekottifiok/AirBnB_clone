#!/usr/bin/python3
"""
State test module
"""
from unittest import TestCase, main
from datetime import datetime
from models.state import State


class test_State(TestCase):
    """
    Unittest for the class State
    """

    def test_init(self):
        """
        unittest for the instantiation of the Amenity
        :return: None
        """
        _state = State()
        self.assertIsNotNone(_state)
        self.assertIsNotNone(_state, State)
        self.assertTrue(hasattr(_state, 'id'))
        self.assertTrue(hasattr(_state, 'created_at'))
        self.assertTrue(hasattr(_state, 'updated_at'))
        _state_dict = _state.to_dict()

        # testing *args and **kwargs
        new_state = State(**_state_dict)
        self.assertIsNotNone(new_state)
        self.assertIsInstance(new_state, State)
        self.assertTrue(hasattr(new_state, 'id'))
        self.assertTrue(hasattr(new_state, 'created_at'))
        self.assertTrue(hasattr(new_state, 'updated_at'))

    def test_save(self):
        """
        unittest for the save method of the Amenity class
        :return:
        """
        _state = State()
        _state.updated_at = datetime(2018, 2, 28, 2, 6, 55, 258896)
        date_stored = _state.updated_at
        _state.save()
        self.assertNotEqual(date_stored, _state.updated_at)

    def test_to_dict(self):
        """
        Unittest for the to_dict method of the Amenity class
        :return:
        """
        _state = State()
        self.assertDictEqual(_state.to_dict(), {
            'id': _state.id,
            'created_at': _state.created_at.isoformat(),
            'updated_at': _state.updated_at.isoformat(),
            '__class__': _state.__class__.__name__
        })

    def test_public_attr(self):
        """

        :return:
        """
        _state = State()
        _state.name = "trial_name"
        self.assertEqual(_state.name, 'trial_name')


if __name__ == "__main__":
    main()
