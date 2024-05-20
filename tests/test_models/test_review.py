#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        ins = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(ins))
        self.assertNotIn("place_id", ins.__dict__)

    def test_user_id_is_public_class_attribute(self):
        ins = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(ins))
        self.assertNotIn("user_id", ins.__dict__)

    def test_text_is_public_class_attribute(self):
        ins = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(ins))
        self.assertNotIn("text", ins.__dict__)

    def test_two_reviews_unique_ids(self):
        ins1 = Review()
        ins2 = Review()
        self.assertNotEqual(ins1.id, ins2.id)

    def test_two_reviews_different_created_at(self):
        ins1 = Review()
        sleep(0.05)
        ins2 = Review()
        self.assertLess(ins1.created_at, ins2.created_at)

    def test_two_reviews_different_updated_at(self):
        ins1 = Review()
        sleep(0.05)
        ins2 = Review()
        self.assertLess(ins1.updated_at, ins2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        ins = Review()
        ins.id = "200359"
        ins.created_at = ins.updated_at = dt
        insstr = ins.__str__()
        self.assertIn("[Review] (200359)", insstr)
        self.assertIn("'id': '200359'", insstr)
        self.assertIn("'created_at': " + dt_repr, insstr)
        self.assertIn("'updated_at': " + dt_repr, insstr)

    def test_args_unused(self):
        ins = Review(None)
        self.assertNotIn(None, ins.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        ins = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ins.id, "345")
        self.assertEqual(ins.created_at, dt)
        self.assertEqual(ins.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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
        ins = Review()
        sleep(0.05)
        first_updated_at = ins.updated_at
        ins.save()
        self.assertLess(first_updated_at, ins.updated_at)

    def test_two_saves(self):
        ins = Review()
        sleep(0.05)
        first_updated_at = ins.updated_at
        ins.save()
        second_updated_at = ins.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        ins.save()
        self.assertLess(second_updated_at, ins.updated_at)

    def test_save_with_arg(self):
        ins = Review()
        with self.assertRaises(TypeError):
            ins.save(None)

    def test_save_updates_file(self):
        ins = Review()
        ins.save()
        insid = "Review." + ins.id
        with open("file.json", "r") as f:
            self.assertIn(insid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ins = Review()
        self.assertIn("id", ins.to_dict())
        self.assertIn("created_at", ins.to_dict())
        self.assertIn("updated_at", ins.to_dict())
        self.assertIn("__class__", ins.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ins = Review()
        ins.middle_name = "Boudan"
        ins.my_number = 98
        self.assertEqual("Boudan", ins.middle_name)
        self.assertIn("my_number", ins.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ins = Review()
        ins_dict = ins.to_dict()
        self.assertEqual(str, type(ins_dict["id"]))
        self.assertEqual(str, type(ins_dict["created_at"]))
        self.assertEqual(str, type(ins_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        ins = Review()
        ins.id = "200359"
        ins.created_at = ins.updated_at = dt
        tdict = {
            'id': '200359',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(ins.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ins = Review()
        self.assertNotEqual(ins.to_dict(), ins.__dict__)

    def test_to_dict_with_arg(self):
        ins = Review()
        with self.assertRaises(TypeError):
            ins.to_dict(None)


if __name__ == "__main__":
    unittest.main()
