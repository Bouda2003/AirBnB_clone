#!/usr/bin/python3
"""amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize a new instance"""
        super().__init__(*args, **kwargs)
