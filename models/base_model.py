#!/usr/bin/python3
import uuid
from datetime import datetime

""""
This modeule contains a base class that contains all
attributes for other classes
Author: Nafeesah and Yebo
"""
class BaseModel():
    """
    A class which contains all attributes for others.

    Attributes:
        id(str): identification for each instances
        created_at(date): current datetime when an instance is created
        updated_at(date): current datetime when an instance is created and updated

    Methods:
        save(): updates the public instance attribute updated_at with the current datetime
        to_dict(): returns a dictionary containing all keys/values of __dict__

    Example:

    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __init__(self, *args, **kwargs):
        """To initialize class attributes"""
        if kwargs:
            for keys,vals in kwargs.items():
                if keys != '__class__':
                    setattr(self, keys, vals)
        else:
            self.id = self.__class__.id
            self.created_at = self.__class__.created_at
            self.updated_at = self.__class__.updated_at
    
    def __str__(self):
        """To overwrite"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        return (self.updated_at)
    
    def to_dict(self):
        """ 
        returns a dictionary containing all keys/values of __dict__ of 
        the instance
        """
        dic = {}
        for key,val in self.__dict__.items():
            if key == 'created_at':
                val1 = val.isoformat()
                dic[key] = val1
            elif key == 'updated_at':
                val2 = val.isoformat()
                dic[key] = val2
            else:
                dic[key] = val
        dic['__class__'] = str(self.__class__.__name__)
        return (dic)
