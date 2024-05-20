#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(ins))
        self.assertNotIn("city_id", ins.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(ins))
        self.assertNotIn("name", ins.__dict__)

    def test_description_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(ins))
        self.assertNotIn("desctiption", ins.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(ins))
        self.assertNotIn("number_rooms", ins.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(ins))
        self.assertNotIn("number_bathrooms", ins.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(ins))
        self.assertNotIn("max_guest", ins.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(ins))
        self.assertNotIn("price_by_night", ins.__dict__)

    def test_latitude_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(ins))
        self.assertNotIn("latitude", ins.__dict__)

    def test_longitude_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(ins))
        self.assertNotIn("longitude", ins.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        ins = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(ins))
        self.assertNotIn("amenity_ids", ins.__dict__)

    def test_two_places_unique_ids(self):
        ins1 = Place()
        ins2 = Place()
        self.assertNotEqual(ins1.id, ins2.id)

    def test_two_places_different_created_at(self):
        ins1 = Place()
        sleep(0.05)
        ins2 = Place()
        self.assertLess(ins1.created_at, ins2.created_at)

    def test_two_places_different_updated_at(self):
        ins1 = Place()
        sleep(0.05)
        ins2 = Place()
        self.assertLess(ins1.updated_at, ins2.updated_at)

    def test_str_representation(self):
        tdt = datetime.today()
        tdt_repr = repr(tdt)
        ins = Place()
        ins.id = "123456"
        ins.created_at = ins.updated_at = tdt
        plstr = ins.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + tdt_repr, plstr)
        self.assertIn("'updated_at': " + tdt_repr, plstr)

    def test_args_unused(self):
        ins = Place(None)
        self.assertNotIn(None, ins.__dict__.values())

    def test_instantiation_with_kwargs(self):
        tdt = datetime.today()
        dt_iso = tdt.isoformat()
        ins = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ins.id, "345")
        self.assertEqual(ins.created_at, tdt)
        self.assertEqual(ins.updated_at, tdt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        ins = Place()
        sleep(0.05)
        first_updated_at = ins.updated_at
        ins.save()
        self.assertLess(first_updated_at, ins.updated_at)

    def test_two_saves(self):
        ins = Place()
        sleep(0.05)
        first_updated_at = ins.updated_at
        ins.save()
        second_updated_at = ins.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        ins.save()
        self.assertLess(second_updated_at, ins.updated_at)

    def test_save_with_arg(self):
        ins = Place()
        with self.assertRaises(TypeError):
            ins.save(None)

    def test_save_updates_file(self):
        ins = Place()
        ins.save()
        insid = "Place." + ins.id
        with open("file.json", "r") as f:
            self.assertIn(insid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ins = Place()
        self.assertIn("id", ins.to_dict())
        self.assertIn("created_at", ins.to_dict())
        self.assertIn("updated_at", ins.to_dict())
        self.assertIn("__class__", ins.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ins = Place()
        ins.middle_name = "Bouda"
        ins.my_number = 98
        self.assertEqual("Bouda", ins.middle_name)
        self.assertIn("my_number", ins.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ins = Place()
        pl_dict = ins.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        tdt = datetime.today()
        ins = Place()
        ins.id = "123456"
        ins.created_at = ins.updated_at = tdt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': tdt.isoformat(),
            'updated_at': tdt.isoformat(),
        }
        self.assertDictEqual(ins.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ins = Place()
        self.assertNotEqual(ins.to_dict(), ins.__dict__)

    def test_to_dict_with_arg(self):
        ins = Place()
        with self.assertRaises(TypeError):
            ins.to_dict(None)


if __name__ == "__main__":
    unittest.main()
