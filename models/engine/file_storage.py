#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        tmp = {}
        for key, val in FileStorage.__objects.items():
            if type(val) is cls:
                tmp[key] = val
        return tmp

    def find_by_id(self, id, cls):
        if id and cls:
            key = cls.__name__ + '.' + id
            if key in FileStorage.__objects:
                return FileStorage.__objects[key]
            return None
        return None

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update(
                {obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.__objects[key] = classes[val['__class__']](
                            **val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside
        if obj is equal to None, the method should not do anything"""
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def count(self, cls):
        """
        counts objects of type cls or all objects of all types
        if cls is None
        """
        count = 0
        if cls:
            for obj in FileStorage.__objects.values():
                if type(obj) is cls:
                    count += 1
        return count

    def close(self):
        """
        call reload() method for deserializing the JSON file to objects
        """
        self.reload()
