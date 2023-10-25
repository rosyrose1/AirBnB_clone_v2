#!/usr/bin/python3
""" Place """

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test for Place module """

    def __init__(self, *args, **kwargs):
        """ instantiation """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test for city id """
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test for user id"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ test for name """
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ test for description """
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test for number of rooms """
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test for number of bathrooms """
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test for maximum guests """
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test for price by night """
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test for latitude"""
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test for Longitude """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test for amenity id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
