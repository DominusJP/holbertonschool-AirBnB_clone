#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

class Tests_FileStorage(unittest.TestCase):
    """
    tests of FileStorage class:
        - test 'all'
        - test 'new'
        - test 'save'
        - test 'reload'
    """

    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "file.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.storage.new(self.base_model)
        obj_key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertTrue(obj_key in self.storage.all())

    def test_save(self):
        self.storage.new(self.base_model)
        self.storage.save()
        obj_key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertTrue(obj_key in self.storage.all())

    def test_reload(self):
        self.storage.new(self.base_model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        obj_key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertTrue(obj_key in new_storage.all())