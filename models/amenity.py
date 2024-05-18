#!/usr/bin/python3
"""Defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amentiy
    Attributes:
        Name(str): the name of amenity
    """

    name = ""
