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
from models.base_model import BaseModel


class TestBaseModel_instant(unittest.TestCase):
    """Testing instants in the BaseModel class"""

    def Test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instant(self):
        self.assertIn(BaseModel(), models.storage.all().values())

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
        insstr = ins.__str__()
        self.assertIn("[BaseModel] (200359)", insstr)
        self.assertIn("'id': '200359'", insstr)
        self.assertIn("'created_at': " + tdt_repr, insstr)
        self.assertIn("'updated_at': " + tdt_repr, insstr)

    def test_unused_args(self):
        ins = BaseModel(None)
        self.assertNotIn(None, ins.__dict__.values())

    def test_instantion_with_Kwargs(self):
        tdt = datetime.today()
        tdt_iso = tdt.isoformat()
        ins = BaseModel(id="200359", created_at=tdt_iso, updated_at=tdt_iso)
        self.assertEqual(ins.id, "200359")
        self.assertEqual(ins.created_at, tdt)
        self.assertEqual(ins.updated_at, tdt)


class Test_BaseModel_save(unittest.TestCase):
    """Testing save method in BaseModel"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save1(self):
        ins = BaseModel()
        sleep(0.1)
        first_updated_at = ins.updated_at
        ins.save()
        self.assertLess(first_updated_at, ins.updated_at)

    def test_save2(self):
        ins = BaseModel()
        sleep(0.1)
        first_updated_at = ins.updated_at
        ins.save()
        second_updated_at = ins.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.1)
        ins.save()
        self.assertLess(second_updated_at, ins.updated_at)

    def test_save_with_args(self):
        ins = BaseModel()
        with self.assertRaises(TypeError):
            ins.save(None)

    def test_save_updates_file(self):
        ins = BaseModel()
        ins.save()
        insid = "BaseModel." + ins.id
        with open("file.json", "r") as f:
            self.assertIn(insid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        ins = BaseModel()
        self.assertTrue(dict, type(ins.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ins = BaseModel()
        self.assertIn("id", ins.to_dict())
        self.assertIn("created_at", ins.to_dict())
        self.assertIn("updated_at", ins.to_dict())
        self.assertIn("__class__", ins.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ins = BaseModel()
        ins.name = "Bouda"
        ins.my_number = 30
        self.assertIn("name", ins.to_dict())
        self.assertIn("my_number", ins.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ins = BaseModel()
        ins_dict = ins.to_dict()
        self.assertEqual(str, type(ins_dict["created_at"]))
        self.assertEqual(str, type(ins_dict["updated_at"]))

    def test_to_dict_output(self):
        tdt = datetime.today()
        ins = BaseModel()
        ins.id = "200359"
        ins.created_at = ins.updated_at = tdt
        tdict = {
            'id': '200359',
            '__class__': 'BaseModel',
            'created_at': tdt.isoformat(),
            'updated_at': tdt.isoformat()
        }
        self.assertDictEqual(ins.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ins = BaseModel()
        self.assertNotEqual(ins.to_dict(), ins.__dict__)

    def test_to_dict_with_arg(self):
        ins = BaseModel()
        with self.assertRaises(TypeError):
            ins.to_dict(None)


if __name__ == "__main__":
    unittest.main()
