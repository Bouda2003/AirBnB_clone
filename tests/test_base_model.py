#!/bin/usr/python3
"""unittesting for models/base_model.py

    Unittest for class: TestBaseModel_instant,
    TestBaseModel_save,
    TestBaseModel_to_dict
"""

import os
import models
import unittest
from time import sleep
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
        ins1 = BaseModel()
        ins2 = BaseModel()
        self.assertNotEqual(ins1.id, ins2.id)

    def test_two_models_created_at(self):
        ins1 = BaseModel()
        sleep(0.1)
        ins2 = BaseModel()
        self.assertLess(ins1.created_at, ins2.created_at)

    def test_two_models_updated_at(self):
        ins1 = BaseModel()
        sleep(0.1)
        ins2 = BaseModel()
        self.assertLess(ins1.updated_at, ins2.updated_at)

    def test_str_representaion(self):
        tdt = datetime.today()
        tdt_repr = repr(tdt)
        ins = BaseModel()
        ins.id = "200359"
        ins.created_at = ins.updated_at = tdt
        insstr= ins.__str__()
        self.assertIn("[BaseModel] (200359)", insstr)
        self.assertIn("'id': '200359'", insstr)
        self.assertIn("'created_at':" + tdt_repr, insstr)
        self.assertIn("'updated_at':" + tdt_repr, insstr)
    def test_unused_args(self):
        ins = BaseModel(None)
        self.assertNotIn(None, ins.__dict__.values())

    def test_instantion_without_Kwargs(self):
        
