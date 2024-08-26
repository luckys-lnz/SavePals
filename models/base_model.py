#!/usr/bin/python3
"""
This module defines a base class for all models in our SavePals application
"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class BaseModel:
    """A base class for all SavePals models"""
    id = Column(String(60), primary_key=True, nullable=False,
                default=generate_uuid)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initializes a new model"""
        if kwargs:
            # Remove 'id', 'created_at', and 'updated_at' from kwargs
            kwargs.pop('id', None)
            kwargs.pop('created_at', None)
            kwargs.pop('updated_at', None)

            # set attribute to the instance
            for attr_name, attr_value in kwargs.items():
                setattr(self, attr_name, attr_value)

    def save(self):
        """ Update the time then save object to storage """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def update(self, cls, **kwargs):
        """ Updates an object attributes and save in storage
            Args:
                 cls (class): The class of the object to update.
                 **kwargs: Key-value pairs of attributes to update.
        """
        obj_id = kwargs.get('id')
        if obj_id is None:
            raise ValueError(
                "The 'id' of the object to update must be provided in kwargs.")

        # Remove 'id' from kwargs to pass only attributes to storage.update
        kwargs.pop('id')

        # Update the object in storage
        storage.update(cls, obj_id, kwargs)

    def to_dict(self):
        """
        Returns: dictionary containing all key/values of __dict__ of the
        instance
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                obj_dict[key] = datetime.isoformat(value)
            else:
                obj_dict[key] = value
        obj_dict["__class__"] = type(self).__name__
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']

        return obj_dict

    def delete(self):
        """Deletes the current instance from storage"""
        from models import storage
        storage.delete(self)
