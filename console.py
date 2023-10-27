#!/usr/bin/python3
"""
console for the project
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class to program the different commands
    """
    models = ["BaseModel", "User", "State", "City",
              "Amenity", "Place", "Review"]
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
        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.models:
            print("** class doesn't exist **")

        else:
            obj = eval(arg[0]+"()")
            obj.save()
            print(obj.id)

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

    def do_create_user(self, arg):
        """
        Create a new instance of User
        """
        new_user = User()
        new_user.save()
        print(new_user.id)

    def do_show_user(self, arg):
        """
        Show details of a User instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** instance id missing **")
            return
        user_id = args[0]
        obj_dict = storage.all()
        key = f"User.{user_id}"
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no User instance found **")

    def do_destroy_user(self, arg):
        """
        Delete a User instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** instance id missing **")
            return
        user_id = args[0]
        obj_dict = storage.all()
        key = f"User.{user_id}"
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no User instance found **")

    def do_update_user(self, arg):
        """
        Update attributes of a User instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** instance id missing **")
            return
        user_id = args[0]
        obj_dict = storage.all()
        key = f"User.{user_id}"
        if key in obj_dict:
            if len(args) < 2:
                print("** attribute name missing **")
                return
            if len(args) < 3:
                print("** value missing **")
                return
            attribute = args[1]
            value = args[2].strip('"')
            setattr(obj_dict[key], attribute, value)
            storage.save()
        else:
            print("** no User instance found **")

    def do_all_user(self, arg):
        """
        List all User instances
        """
        obj_dict = storage.all()
        user_list = [str(obj) for obj in obj_dict.values() if obj.__class__.__name__ == 'User']
        print(user_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
