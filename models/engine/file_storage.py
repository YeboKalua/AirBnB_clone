#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

"""
This module contains function that
serializes and deserializes to store data created by users
Author: Nafeesah and Yebo
"""


class FileStorage():
    """
    A class that is used to serialize and deserialize and store in a file

    Attributes:
        file_path(str): string - path to the JSON file (ex: file.json)
        objects(dictionary): - empty but will store all objects by class

    Methods:
        all(): returns the dictionary __objects
        new(): sets in __objects the obj with key <obj class name>.id
        save(): serializes __objects to the JSON file (path: __file_path)
        reload(): deserializes the JSON file to __objects
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """To initialize objects"""
        self.__file_path = self.__class__.__file_path
        self.__objects = self.__class__.__objects

    def all(self):
        """retutns the dictionary objcts"""
        return self.__objects

    def new(self, obj):
        """sets in new value into objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        filename = self.__file_path
        with open(filename, "w") as file:
            objects_dict = {}
            for key, value in self.__objects.items():
                objects_dict[key] = self.__objects[key].to_dict()
            json.dump(objects_dict, file)

    def reload(self):
        """deserializes the JSON file to objects"""
        filename = self.__file_path

        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            content = file.read()
            if content is None:
                return
            objects_dict = json.loads(content)
            self.__objects = {}
            for key, value in objects_dict.items():
                self.__objects[key] = BaseModel(**objects_dict[key])
