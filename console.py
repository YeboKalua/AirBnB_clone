#!/usr/bin/python3
import cmd

"""
This module is for the console
to create interactive and non-interactive mode
Author: Yebo and Nafeesah
"""


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
    prompt = ''

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Exit program on running EOF"""
        print()
        return True
    
    def help_quit(self):
        """Displays what quit does"""
        print ('\n').join([
            'Quit command to exit the program'
        ])
    
    def do_prompt(self):
        """Print prompt"""
        self.prompt = '(hbnb) '

    def emptyline(self):
        """
        implements what happens when an emptyline is used as command
        """
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()