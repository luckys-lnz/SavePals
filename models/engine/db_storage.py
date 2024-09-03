#!/usr/bin/python3
"""
Module defines Database engine `DBStorage`
"""
import os
from models.base_model import Base
from models.user import User
from models.group import Group
from models.round_ import Round
from models.payout import Payout
from models.contribution import Contribution
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


# get the environ variabes
user = os.getenv('SAVEPAL_PSQL_USER')
passwd = os.getenv('SAVEPAL_PSQL_PWD')
host = os.getenv('SAVEPAL_PSQL_HOST')
db = os.getenv('SAVEPAL_PSQL_DB')
savepal_env = os.getenv('SAVEPAL_ENV')


# import to test BaseModel -- testing purposes only
if savepal_env == "test":
    from models.base_for_testing import TestBase


class DBStorage:
    """ Defines database engine """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize database instance """
        self.__engine = create_engine(
            f"postgresql+psycopg2://{user}:{passwd}@{host}/{db}",
            pool_pre_ping=True)

        if savepal_env == "test":
            # Drop all tables if test environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects if cls is None or objects of specified class
        """
        objs_dict = {}
        if cls:
            # Handle class
            for obj in self.__session.query(cls).all():
                key = f"{type(obj).__name__}.{obj.id}"
                objs_dict[key] = obj
        else:
            # Handle all classes
            cls_list = [State, City, User, Review, Place, Amenity]
            for cls in cls_list:
                for obj in self.__session.query(cls).all():
                    key = f"{type(obj).__name__}.{obj.id}"
                    objs_dict[key] = obj
        return objs_dict

    def get(self, cls, id):
        """ Retrieves an object based on its class and ID """
        if id is None:
            raise ValueError("ID cannot be None")

        obj = self.__session.query(cls).get(id)

        if obj is None:
            # Handle the case where no object is found
            raise ValueError(f"No object found with ID {id}")

        return obj

    def filter(self, cls, **kwargs):
        """
        Filter all instances of a given class based on the provided criteria.
        """
        # Get all instances of the specified class
        all_objects = self.all(cls).values()

        # Filter objects that match all criteria in kwargs
        filtered_objects = [
            obj for obj in all_objects
            if all(getattr(obj, key) == value for key, value in kwargs.items())
        ]

        return filtered_objects

    def new(self, obj):
        """ Add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the current database session """
        self.__session.commit()

    def count(self, cls):
        """ Counts the number of objects of specified class """
        return self.__session.query(cls).count()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def update(self, cls, obj_id, attr_dict):
        """ Updates an object of a specified class with the given attributes.
            Args:
                 cls (class): The class of the object to update.
                 obj_id (str): The ID of the object to update.
                 attr_dict (dict): A dictionary of attributes to update.
        """
        # Retrieve the object by class and ID
        obj = self.get(cls, obj_id)

        # Update the object's attributes directly
        for key, value in attr_dict.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        # Save changes to the database
        self.__session.commit()

    def reload(self):
        """ Creates all tables and the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """ Removes the current session """
        self.__session.remove()