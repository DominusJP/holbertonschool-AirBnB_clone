#!/usr/bin/python3
"""
console for the project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class to program the different commands
    """
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
        return True

    def emptyline(self):
        """
        command to cover the emptylines in input
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
