#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    fist_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
