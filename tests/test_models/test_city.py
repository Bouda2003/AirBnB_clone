#!/bin/usr/python3
"""unittesting for models/City.py

    Unittest for class: TestCity_instant,
    TestCity_save,
    TestCity_to_dict
"""

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.city import City


class TestCity_instant(unittest.TestCase):
    """Testing instant(City class"""

    def Test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_instant(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_datetime(self):
        self.assertEqual(datetime, type((City).created_at))

    def test_updated_datetime(self):
        self.assertEqual(datetime, type((City).updated_at))

    def test_two_models_unique_id(self):
        ins1 = City()
        ins2 = City()
        self.assertNotEqual(ins1.id, ins2.id)

    def test_two_models_created_at(self):
        ins1 = City()
        sleep(0.1)
        ins2 = City()
        self.assertLess(ins1.created_at, ins2.created_at)

    def test_two_models_updated_at(self):
        ins1 = City()
        sleep(0.1)
        ins2 = City()
        self.assertLess(ins1.updated_at, ins2.updated_at)

    def test_str_representaion(self):
        tdt = datetime.today()
        tdt_repr = repr(tdt)
        ins = City()
        ins.id = "200359"
        ins.created_at = ins.updated_at = tdt
        insstr = ins.__str__()
        self.assertIn("[City] (200359)", insstr)
        self.assertIn("'id': '200359'", insstr)
        self.assertIn("'created_at': " + tdt_repr, insstr)
        self.assertIn("'updated_at': " + tdt_repr, insstr)

    def test_unused_args(self):
        ins = City(None)
        self.assertNotIn(None, ins.__dict__.values())

    def test_instantion_with_Kwargs(self):
        tdt = datetime.today()
        tdt_iso = tdt.isoformat()
        ins = City(id="200359", created_at=tdt_iso, updated_at=tdt_iso)
        self.assertEqual(ins.id, "200359")
        self.assertEqual(ins.created_at, tdt)
        self.assertEqual(ins.updated_at, tdt)

    def test_instantiation_without_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    class Test_City_save(unittest.TestCase):
        """Testing save method in City"""

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
        ins = City()
        sleep(0.1)
        first_updated_at = ins.updated_at
        ins.save()
        self.assertLess(first_updated_at, ins.updated_at)

    def test_save2(self):
        ins = City()
        sleep(0.1)
        first_updated_at = ins.updated_at
        ins.save()
        second_updated_at = ins.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.1)
        ins.save()
        self.assertLess(second_updated_at, ins.updated_at)

    def test_save_with_args(self):
        ins = City()
        with self.assertRaises(TypeError):
            ins.save(None)

    def test_save_updates_file(self):
        ins = City()
        ins.save()
        insid = "City." + ins.id
        with open("file.json", "r") as f:
            self.assertIn(insid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        ins = City()
        self.assertTrue(dict, type(ins.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ins = City()
        self.assertIn("id", ins.to_dict())
        self.assertIn("created_at", ins.to_dict())
        self.assertIn("updated_at", ins.to_dict())
        self.assertIn("__class__", ins.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ins = City()
        ins.name = "Bouda"
        ins.my_number = 30
        self.assertIn("name", ins.to_dict())
        self.assertIn("my_number", ins.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ins = City()
        ins_dict = ins.to_dict()
        self.assertEqual(str, type(ins_dict["created_at"]))
        self.assertEqual(str, type(ins_dict["updated_at"]))

    def test_to_dict_output(self):
        tdt = datetime.today()
        ins = City()
        ins.id = "200359"
        ins.created_at = ins.updated_at = tdt
        tdict = {
            'id': '200359',
            '__class__': 'City',
            'created_at': tdt.isoformat(),
            'updated_at': tdt.isoformat()
        }
        self.assertDictEqual(ins.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ins = City()
        self.assertNotEqual(ins.to_dict(), ins.__dict__)

    def test_to_dict_with_arg(self):
        ins = City()
        with self.assertRaises(TypeError):
            ins.to_dict(None)


if __name__ == "__main__":
    unittest.main()
