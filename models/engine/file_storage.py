#!/usr/bin/python3
"""storage engine"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objets"""
        return self.__objects

    def new(self, obj):
        """adds new object"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """saves objects to file"""
        ser_dict = {}
        for key in self.__objects.keys():
            ser_dict[key] = self.__objects[key].to_dict()
        ser_dict = json.dumps(ser_dict)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(ser_dict)

    def reload(self):
        """reloads objects from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                tmp = json.loads(f.read())
            for key in tmp.keys():
                initiator = eval(key.split('.')[0])
                self.__objects[key] = initiator(**tmp[key])

        except Exception:
            pass
