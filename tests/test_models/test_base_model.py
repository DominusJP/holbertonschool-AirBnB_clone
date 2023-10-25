#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

class Tests_BaseModel(unittest.TestCase):
    """
    tests of BaseModel class
    """
    def test_unique_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.to_dict, obj2.to_dict)

    def test_update_time(self):
        obj1 = BaseModel()
        origin = obj1.to_dict()
        obj1.save()
        self.assertNotEqual(origin, obj1.to_dict)

    def test_str_repr(self):
        obj1 = BaseModel()
        str_obj1 = f"[{type(obj1).__name__}] ({obj1.id}) {obj1.__dict__}"
        self.assertEqual(str(obj1), str_obj1)

    def test_type_returned(self):
        obj1 = BaseModel()
        self.assertEqual(str, type(obj1.__str__()))
        self.assertEqual(dict, type(obj1.to_dict()))
