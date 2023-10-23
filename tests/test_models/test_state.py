#!/usr/bin/python3
""" module that test state.py file """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ A class designed to perform tests on the state.py file. """

    def __init__(self, *args, **kwargs):
        """ Constructor for the test_state class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Additional testing of the state name """
        new = self.value()
        self.assertEqual(type(new.name), str)
