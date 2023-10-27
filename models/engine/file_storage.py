#!/usr/bin/python3
"""
File with class FileStorage
"""
import json
import os


class FileStorage:
    """
    Class used for file storage as name suggests
    """


    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """
        Method that returns the dictionary objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj
    
    def save(self):
        """
        serializes __objects to the JSON file
        """
        new_dict = {}
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as json_file:
            for key in FileStorage.__objects:
                new_dict[key] = (FileStorage.__objects[key]).to_dict()
            json.dump(new_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists.
        """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as json_file:
                # Attempt to open the JSON file in read mode
                obj_dict = json.load(json_file)
                # Load the contents of the JSON file into a dictionary
                for key, value in obj_dict.items():
                    cls = value.get("__class__")
                    new_obj = eval(cls+'(**value)')
                    # Use eval to create an instance of the class based on the class name
                    self.new(new_obj)
        except Exception:
            pass