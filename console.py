#!/usr/bin/python3
"""
This module starts the command interpreter using cmd module.
"""
from models import base_model


class HBNBCommand(cmd.Cmd):
    """This class is the command interpreter.
    It inherits from cmd.
    Cmd which means it can make use of the cmd module.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
