#!/usr/bin/python3
"""Base class that will inherit to all other classes"""
import uuid  # librery for the universal unique identifier
from datetime import datetime  # librery for gettig current date
#from models.engine.file_storage import FileStorage
import models

class BaseModel:
    """Base Model"""

    def __init__(self, *args, **kwargs):
        """Constructor for the Base Model Class,
        now accepting args and kwargs"""
        if kwargs:
            # just checking if kwargs are provided (not empty)
            for key, value in kwargs.items():
                # iterating through the keyword arguments
                if key != '__class__':
                    # checking/excluding the '__class__' key from kargs
                    if key in ['created_at', 'updated_at']:
                        # check if the key is in one of those attributes
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                        # in order to convert the string representation into a daytime object
                    else:
                        setattr(self, key, value)
                        # set new attributes based on new provided values
        else:
            # if not keywards not provided, generate new id, createdat and updated at attributes
            self.id = str(uuid.uuid4())
            # asign universal unique identifier
            self.created_at = datetime.now()
            # assigns current date to the created_at attribute
            self.updated_at = self.created_at
            # assigns current date to the updated_at attribute
        storage.new(self) # set other attributes from kwargs

    def save(self):
        """This line defines a method named save. This method is used
        to update the updated_at attribute with the current date and time
        whenever an instance is modified."""
        self.updated_at = datetime.now() \
            # This line updates the updated_at attribute with the
        # current date and time when the save method is called.
        storage.save() # save the obkect using the storage
        return self.updated_at

    def __str__(self):
        """prints class name followed by id and dict"""
        class_name = self.__class__.__name__ \
            # gets the name of the class as a string
        return (f"[{class_name}] ({self.id}) {self.__dict__}") \
            # prints the class name followed by the id and dict

    def to_dict(self):
        """This method is used to convert the instance's attributes
        into a dictionary for serialization."""
        data = self.__dict__.copy() \
            # creates a copy of the instance's attribute dictionary
        # using self.__dict__
        data['__class__'] = type(self).__name__
        data['created_at'] = self.created_at.isoformat() \
            # adds the created_at attribute to the "data" dictionary
        # in ISO format using the "isoformat" method
        # of the "datetime" objects
        data['updated_at'] = self.updated_at.isoformat() \
            # same thing but for the updated_at attribute
        return data \
            # This line returns the data dictionary, which contains
        # a serialized representation of the instance's attributes.
