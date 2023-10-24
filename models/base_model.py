#!/usr/bin/python3
"""Base class that will inherit to all other classes"""
import uuid  # librery for the universal unique identifier
from datetime import datetime  # librery for gettig current date


class BaseModel:
    """Base Model"""

    def __init__(self):
        """Contructor for the Base Model Class"""
        self.id = str(uuid.uuid4()) \
            # asign universal unique identifier
        self.created_at = datetime.now() \
            # assigns current date to the created_at attribute
        self.updated_at = datetime.now() \
            # assigns current date to the updated_at attribute

    def save(self):
        """This line defines a method named save. This method is used
        to update the updated_at attribute with the current date and time
        whenever an instance is modified."""
        self.updated_at = datetime.now() \
            # This line updates the updated_at attribute with the
        # current date and time when the save method is called.

    def __str__(self):
        """prints class name followed by id and dict"""
        class_name = self.__class__.__name__ \
            # gets the name of the class as a string
        return(f"[{class_name}] ({self.id}) {self.__dict__}") \
            # prints the class name followed by the id and dict

    def to_dict(self):
        """This method is used to convert the instance's attributes
        into a dictionary for serialization."""
        data = self.__dict__ \
            # creates a copy of the instance's attribute dictionary
        # using self.__dict__
        data['created_at'] = self.created_at.isoformat() \
            # adds the created_at attribute to the "data" dictionary
        # in ISO format using the "isoformat" method
        # of the "datetime" objects
        data['updated_at'] = self.updated_at.isoformat() \
            # same thing but for the updated_at attribute
        return data \
            # This line returns the data dictionary, which contains
        # a serialized representation of the instance's attributes.
