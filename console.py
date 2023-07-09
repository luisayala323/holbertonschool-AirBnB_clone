#!/usr/bin/python3
"""This is the console module.

This module starts the command interpreter using cmd module.
"""  # !/usr/bin/python3
"""This is the console module.

This module starts the command interpreter using cmd module.
"""




import cmd
from models import base_model, user, state, city, amenity, place, review, storage
class HBNBCommand(cmd.Cmd):
    """This class is the command interpreter.

    It inherits from cmd.Cmd which means it can make use of the cmd module.
    """

    prompt = '(hbnb) '
    classes = {
        "BaseModel": base_model.BaseModel,
        "User": user.User,
        "State": state.State,
        "City": city.City,
        "Amenity": amenity.Amenity,
        "Place": place.Place,
        "Review": review.Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
