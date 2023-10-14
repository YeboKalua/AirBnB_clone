#!/usr/bin/python3


"""
This module is for the console
to create interactive and non-interactive mode
Author: Yebo and Nafeesah
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    This is the class for the console.

    Attributes:
        prompt(str): (hbnb)

    Methods:
        do_quit(): to quit
        do_prompt(): to print prompt
        do_EOF(): to exit process
    """
    prompt = '(hsnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit program on running EOF"""
        print()
        return True

    def help_quit(self):
        """Displays what quit does"""
        print('Quit ciommand to exit the program\n')

    def emptyline(self):
        """
        implements what happens when an emptyline is used as command
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
