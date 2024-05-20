#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        ins = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(ins))
        self.assertNotIn("name", ins.__dict__)

    def test_two_states_unique_ids(self):
        ins1 = State()
        ins2 = State()
        self.assertNotEqual(ins1.id, ins2.id)

    def test_two_states_different_created_at(self):
        ins1 = State()
        sleep(0.05)
        ins2 = State()
        self.assertLess(ins1.created_at, ins2.created_at)

    def test_two_states_different_updated_at(self):
        ins1 = State()
        sleep(0.05)
        ins2 = State()
        self.assertLess(ins1.updated_at, ins2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        ins = State()
        ins.id = "2003596"
        ins.created_at = ins.updated_at = dt
        ststr = ins.__str__()
        self.assertIn("[State] (2003596)", ststr)
        self.assertIn("'id': '2003596'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_args_unused(self):
        ins = State(None)
        self.assertNotIn(None, ins.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        ins = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ins.id, "345")
        self.assertEqual(ins.created_at, dt)
        self.assertEqual(ins.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

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
        ins = State()
        sleep(0.05)
        first_updated_at = ins.updated_at
        ins.save()
        self.assertLess(first_updated_at, ins.updated_at)

    def test_two_saves(self):
        ins = State()
        sleep(0.05)
        first_updated_at = ins.updated_at
        ins.save()
        second_updated_at = ins.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        ins.save()
        self.assertLess(second_updated_at, ins.updated_at)

    def test_save_with_arg(self):
        ins = State()
        with self.assertRaises(TypeError):
            ins.save(None)

    def test_save_updates_file(self):
        ins = State()
        ins.save()
        insid = "State." + ins.id
        with open("file.json", "r") as f:
            self.assertIn(insid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ins = State()
        self.assertIn("id", ins.to_dict())
        self.assertIn("created_at", ins.to_dict())
        self.assertIn("updated_at", ins.to_dict())
        self.assertIn("__class__", ins.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ins = State()
        ins.middle_name = "Bouda"
        ins.my_number = 98
        self.assertEqual("Bouda", ins.middle_name)
        self.assertIn("my_number", ins.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ins = State()
        ins_dict = ins.to_dict()
        self.assertEqual(str, type(ins_dict["id"]))
        self.assertEqual(str, type(ins_dict["created_at"]))
        self.assertEqual(str, type(ins_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        ins = State()
        ins.id = "2003596"
        ins.created_at = ins.updated_at = dt
        tdict = {
            'id': '2003596',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(ins.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ins = State()
        self.assertNotEqual(ins.to_dict(), ins.__dict__)

    def test_to_dict_with_arg(self):
        ins = State()
        with self.assertRaises(TypeError):
            ins.to_dict(None)


if __name__ == "__main__":
    unittest.main()
