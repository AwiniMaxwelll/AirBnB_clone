#!/usr/bin/python3
"""The base model"""
import uuid
from datetime import datetime as dt

class BaseModel:
    """The parent parent class to all the classes"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            kwargs['created_at'] = dt.strptime(kwargs['created_at'],
                                               '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = dt.strptime(kwargs['updated_at'],
                                               '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if '__class__' not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        """Return the string representation of the BaseModel object"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """return the string representation of the BaseModel class"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates <updated_at> instance with the current datetime"""
        from models import storage
        self.updated_at = dt.now()
        storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of the BaseModel class"""
        cls_dict = dict(self.__dict__)
        cls_dict['__class__'] = self.__class__.__name__
        cls_dict['created_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cls_dict['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return cls_dict
