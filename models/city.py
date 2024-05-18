#!/usr/bin/python3
"""Defines class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city
    Attributes:
        state_id (str): state's id
        name (str): state's name
    """
    state_id = ""
    name = ""
