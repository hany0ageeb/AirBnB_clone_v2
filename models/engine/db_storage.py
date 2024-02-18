#!/usr/bin/python3
"""Thisi module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        conn_url = URL.create(
               'mysql+mysqldb',
               host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
               port=3306,
               username=os.getenv('HBNB_MYSQL_USER'),
               password=os.getenv('HBNB_MYSQL_PWD'),
               database=os.getenv('HBNB_MYSQL_DB'))
        DBStorage.__engine = create_engine(
                conn_url,
                pool_pre_ping=True,
                echo=False)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        dictionary = {}
        instances = []
        classes = (BaseModel, User, Place, State, City, Amenity, Review)
        if cls is None:
            for cla in classes:
                instances.extend(self.__session.query(cla).all())
        else:
            instances = self.__session.query(cla).all()
        for instance in instances:
            key = instance.to_dict()['__class__'] + '.' + instance.id
            dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(session_factory)
