#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        ser_dict = {}
        for key in self.__objects.keys():
            ser_dict[key] = self.__objects[key].to_dict()
        ser_dict = json.dumps(ser_dict)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(ser_dict)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                tmp = json.loads(f.read())
            for key in tmp.keys():
                initiator = eval(key.split('.')[0])
                self.__objects[key] = initiator(**tmp[key])
                """if tmp[key]["__class__"] == "BaseModel":
                    self.__objects[key] = BaseModel(**tmp[key])"""

        except:
            pass
