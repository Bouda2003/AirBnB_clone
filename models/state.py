#!/usr/bin/python3
"""state model"""
from models.base_model import BaseModel


class State(BaseModel):
    """state classs"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize a new instance"""
        super().__init__(*args, **kwargs)
