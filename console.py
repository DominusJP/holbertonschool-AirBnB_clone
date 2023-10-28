#!/usr/bin/python3
"""
console for the project
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class to program the different commands
    """
    models = ["BaseModel", "User", "State", "City",
              "Amenity", "Place", "Review", "User"]
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        command to quit the console
        """
        return True

    def do_EOF(self, arg):
        """
        command to signal the end of input in the console
        and therefore, exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        command to cover the emptylines in input
        """
        pass

    def do_create(self, *args):
        """
        creates a new instance of an object
        """
        arg = args[0].split()
        class_name = arg[0]
        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")

        elif class_name in globals():
            obj = globals()[class_name]()
            # globals is a built in function including all of the
            # variables and their values
            obj.save()
            print(obj.id)
        elif class_name not in globals():
            print("** class doesn't exist **")

    def do_show(self, *args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        arg = args[0].split()
        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")

        elif len(arg) == 1 and arg[0] in HBNBCommand.models:
            print("** instance id missing **")

        elif len(arg) < 2:
            print("** instance id missing **")

        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, *args):
        """
        Deletes an instance based on the class name and id
        """
        arg = args[0].split()
        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")

        elif len(arg) == 1 and arg[0] in HBNBCommand.models:
            print("** instance id missing **")

        elif len(arg) < 2:
            print("** instance id missing **")

        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[key]
                storage.save()
                
    def do_all(self, *args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg = args[0].split()
        obj_dict = storage.all()
        obj_list = []
        if len(args[0]) == 0:
            for key in obj_dict:
                obj_list.append(str(obj_dict[key]))
            print(obj_list)
        else:
            if arg[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
            else:
                for key, value in obj_dict.items():
                    if (value.to_dict()).get('__class__') == arg[0]:
                        obj_list.append(str(obj_dict[key]))
                print(obj_list)

    def do_update(self, *args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        arg = args[0].split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                setattr(obj_dict[key], arg[2], arg[3].strip('"'))
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
