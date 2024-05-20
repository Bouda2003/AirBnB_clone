#!/usr/bin/python3
"""Defines the base model for all"""
import json
import uuid
import datetime
import models


class BaseModel:
    """base model class"""
    def __init__(self, *args, **kwargs):
        """initiating an instance"""
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            self.__dict__.update(kwargs)
            self.created_at = datetime.datetime.
                    fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.datetime.
                    fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """saves changes"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict representaion of the obj"""
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict
