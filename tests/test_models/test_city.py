#!/usr/bin/python3
"""Defining a test class for city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ This class contains tests for the city class """

    def __init__(self, *args, **kwargs):
        """ Initializes an instance of test_city """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Tests the state_id attribute of city instances. """
        new = self.value()
        self.assertNotEqual(type(new.state_id), str)

    def test_name(self):
        """ Tests the name attribete of city instances. """
        new = self.value()
        self.assertNotEqual(type(new.name), str)
