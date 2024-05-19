#!/bin/usr/python3
"""unittesting for models/base_model.py

    Unittest for class: TestBaseModel_instant,
    TestBaseModel_save,
    TestBaseModel_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from models.base_modle import BaseModel


class TestBaseModel_instant(unittest.TestCase):
    """Testing instants in the BaseModel class"""

    def Test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instant(self):
        self.assertIn(BaseModel(), type(BaseModel(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_id(self):
