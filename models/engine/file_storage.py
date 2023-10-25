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
    def __init__(self):
        """
        Constructor for the FileStorage class
        """
        self.__objects = {}
    
    def all(self):
        """
        Method that returns the dictionary objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """
        serializes __objects to the JSON file
        """
        ser_data = {}
        for key, value in self.__objects.items():
            ser_data[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(ser_data, file)

    def reload(self):
        """
        .
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file: \
                # 'r' makes it so that the file is opened for reading. with to /
                # make sure the file is correctly opened and closed
                    deser_data = json.loads(self.__file_path)
                for key, value in deser_data.items:
                    class_name, obj_id = key.split(".")
                    # splits the key in two parts, 
                    # to extract the class_name and obj id
                    cls = models[class_name]
                    self.__objects[key] = cls(**value)
                    # Creates a new instance of the class using value as argument
                    # storing it in the __objects dictionary
            except Exception:
                pass
