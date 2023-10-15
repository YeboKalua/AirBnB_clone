#!/usr/bin/python3
"""to import basemodel"""
from models.base_model import BaseModel
"""
This module contains the class User.
It contains users attributes
Author: Nafeesah and Yebo
"""


class User(BaseModel):
    """
    A class that contains the detail of user.

    Attributes:
        email(str): empty string
        password(str): empty string
        first_name(str): empty string
        last_name(str): empty string

    Methods:
        None
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
