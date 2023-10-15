#!/usr/bin/python3


"""
This module is for the console
to create interactive and non-interactive mode
Author: Yebo and Nafeesah
"""


import cmd
from models import storage
from models.base_model import BaseModel

class_name = [
    'BaseModel'
]
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

    def do_create(self,command):
        """Creates a new instance of BaseModel"""
        if command == "":
            print("** class name missing **")
        elif command not in class_name:
            print("** class doesn't exist **")
        else:
            if command == "BaseModel":
                instance = BaseModel()
        
        instance.save()
        print(instance.id)

    def help_create(self):
        """Displays what create does"""
        print("Creates a new instance of a class\n")
    
    def do_show(self, command):
        """Prints the string representation of an instance """
        args = command.split(" ")

        if args[0] == "":
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in class_name:
            print("** class doesn't exist **")
        else:
            classname = args[0]
            instance_id = args[1]
            instance_key = "{}.{}".format(classname, instance_id)
            if instance_key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[instance_key])

    def help_show(self):
        """Displays what show does"""
        print("Shows an instance of a class\n")
    
    def do_destroy(self, command):
        """Destroys an instance of a class"""
        args = command.split(" ")

        if args[0] == "":
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in class_name:
            print("** class doesn't exist **")
        else:
            classname = args[0]
            instance_id = args[1]
            instance_key = "{}.{}".format(classname, instance_id)
            if instance_key not in storage.all():
                print("** no instance found **")
                return
            
            del storage.all()[instance_key]
            storage.save()

    def help_destroy(self):
        """Displays what destroy does"""
        print("Destroys an instance of a class\n")

    def do_all(self, command):
        """Prints all string representation of all instances"""
        args = command.split(" ")

        if args[0] != "" and args[0] not in class_name:
            print("** class doesn't exist **")
        else:
            class_filter = args[0] if args[0] else None
            all_list = [
                str(vals) for key, vals in storage.all().items()
                if not class_filter or key.startswith(class_filter)
                ]
            print(all_list)

    def help_all(self):
        """Displays what all does"""
        print("Displays instances of a class or all classes\n")

    def do_update(self, command):
        args = command.split(" ")

        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in class_name:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            classname = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            instance_key = "{}.{}".format(classname, instance_id)
            if instance_key not in storage.all():
                print("** no instance found **")
                return
            
            instance = storage.all()[instance_key]
            if attribute_name not in instance.to_dict():
                setattr(instance, attribute_name, args[3])
            else:
                set_attr = type(getattr(instance, attribute_name))(args[3])
                setattr(instance, attribute_name, set_attr)
            storage.save()

    def help_update(self):
        """Displays what update does"""
        print("Updates instances of a class\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
