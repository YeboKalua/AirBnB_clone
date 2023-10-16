#!/usr/bin/python3
"""to import basemodel"""
from models.base_model import BaseModel
"""
This module contains the class Review.
It contains review attributes
Author: Nafeesah and Yebo
"""


class Review(BaseModel):
    """
    A class that contains the details of review.

    Attributes:
        place_id(str): it will be the Place.id
        user_id(str): it will be the User.id
        text(str): empty string

    Methods:
        None
    """

    place_id = ""
    user_id = ""
    text = ""
