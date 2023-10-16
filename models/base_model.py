#!/usr/bin/python3

""""
This modeule contains a base class that contains all
attributes for other classes
Author: Nafeesah and Yebo
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    A class which contains all attributes for others.

    Attributes:
        id(str): identification for each instances
        created_at(date): current datetime when an instance is created
        updated_at(date): current datetime when an instance is updated

    Methods:
        save(): updates updated_at with the current datetime
        to_dict(): returns a dictionary containing all keys/values of __dict__

    Example:

    """

    def __init__(self, *args, **kwargs):
        """To initialize class attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for keys, vals in kwargs.items():
                if keys != '__class__':
                    if (
                            keys
                            in ['created_at', 'updated_at']
                            and isinstance(vals, str)
                    ):
                        form = '%Y-%m-%dT%H:%M:%S.%f'
                        val_datetime = datetime.strptime(vals, form)
                        setattr(self, keys, val_datetime)
                    else:
                        setattr(self, keys, vals)
        else:
            models.storage.new(self)

    def __str__(self):
        """To overwrite"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of
        the instance
        """
        dic = {}
        for key, val in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dic[key] = val.isoformat()
            else:
                dic[key] = val
        dic['__class__'] = self.__class__.__name__
        return (dic)
