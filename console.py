#!/usr/bin/python3
"""Define Airbnb console"""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Defines the hbnb command interpreter
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb)"
    used_classes = ["BaseModel", "User", "State", "City", "place", "Amenity", "Review"]


    def emptyline(self):
        """I think Iam blind"""
        pass
    def do_quit(self, arg):
        "Iam freeeeeeeeeeeeee"
        return True
    def do_EOF(self, arg):
        """sent Help!!! ahhhhhhhhhhh!"""
        print("")
        return True
    def help_quit(self, arg):
        """press quit to exit you stu..."""
        print("Press Quit command to exit the program")
        return True
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
            usage: create <class_name>
        """
        Tokens = split(arg)
        if len(Tokens) == 0:
            print("** class name missing **")
        elif Tokens[0] not in HBNBCommand.used_classes:
            print("** class doesn't exist **")
        else:
            new_ins = BaseModel()
            new_ins.save()
            print(new_ins.id)
    def do_show(self, arg):
        """shows the string representation of an instance based on the class name
            usage: show <class_name> <id>
        """
        Tokens = split(arg)
        Dict = storage.all()
        if len(Tokens) == 0:
            print("** class name missing **")
        elif Tokens[0] not in HBNBCommand.used_classes:
            print("** class doesn't exist **")
        elif len(Tokens) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(Tokens[0], Tokens[1]) not in Dict:
            print("** no instance found **")
        else:
            print(Dict["{}.{}".format(Tokens[0], Tokens[1])])
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)
            usage: destroy <class_name> <id>
        """
        Tokens = split(arg)
        Dict = storage.all()
        if len(Tokens) == 0:
            print("** class name missing **")
        elif Tokens[0] not in HBNBCommand.used_classes:
            print("** class doesn't exist **")
        elif len(Tokens) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(Tokens[0], Tokens[1]) not in Dict:
            print("** no instance found **")
        else:
            del Dict["{}.{}".format(Tokens[0], Tokens[1])]
            storage.save()
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name.
            usage: all [class_name]
        """
        Tokens = split(arg)
        List = []
        if len(Tokens) == 0:
            List = [str(obj) for obj in storage.all().values()]
        elif Tokens[0] in HBNBCommand.used_classes:
            List = [str(obj) for obj in storage.all().values() if type(obj).__name__ == Tokens[0]]
        else:
            print("** class doesn't exist **")
            return
        print(List)
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
            usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        Tokens = split(arg)
        if len(Tokens) == 0:
            print("** class name missing **")
        elif Tokens[0] not in HBNBCommand.used_classes:
            print("** class doesn't exist **")
        elif len(Tokens) == 1:
            print("** instance id missing **")
        elif len(Tokens) == 2:
            print("** attribute name missing **")
        elif len(Tokens) == 3:
            print("** value missing **")
        else:
            class_name, instance_id, attr_name, attr_value = Tokens[0], Tokens[1], Tokens[2], Tokens[3]
            if class_name not in HBNBCommand.used_classes:
                print("** class doesn't exist **")
                return
            key = f"{class_name}.{instance_id}"
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
                return
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                attr_value = attr_type(attr_value)
            else:
                attr_value = str(attr_value)
            setattr(obj, attr_name, attr_value)
            obj.save()
if __name__ == '__main__':
        HBNBCommand().cmdloop()
