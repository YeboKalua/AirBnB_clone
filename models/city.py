#!/usr/bin/python3
"""to import basemodel"""
from models.base_model import BaseModel
"""
This module contains the class city.
It contains city attributes.
Author: Nafeesah and Yebo
"""

class City(BaseModel):
    """
    A class that contains the details of city.

    Attributes:
        state_id(str): it will be the State.id
        name(str): empty string

    Methods:
        None
    """

    state_id = ""
    name = ""