#!/usr/bin/python3
"""review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize a new instance"""
        super().__init__(*args, **kwargs)
