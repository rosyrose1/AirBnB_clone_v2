#!/usr/bin/python3
"""Defining a test class for review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ This class contains tests for the review class """

    def __init__(self, *args, **kwargs):
        """Initializes an instance of test_review """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Tests the place_id attribute review instance """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Tests the user_id attribute of review instances. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Tests the text attribute of review instances. """
        new = self.value()
        self.assertEqual(type(new.text), str)
