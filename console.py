#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that contains the entry point of the command interpreter
    """

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] == "update":
                    args = split(command[1])
                    if len(args) < 3:
                        print('** missing arguments **')
                    else:
                        class_name = argl[0]
                        obj_id = args[0]
                        attr_name = args[1]
                        attr_value = args[2].strip('"')
                        if class_name not in self.classes:
                            print("** class doesn't exist **")
                        else:
                            key = f"{class_name}.{obj_id}"
                            all_objs = storage.all()
                            if key not in all_objs:
                                print('** no instance found **')
                            else:
                                obj = all_objs[key]
                                setattr(obj, attr_name, attr_value)
                                obj.save()
                        return
                elif command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            else:
                del all_objs[key]
                storage.save()

    def do_all(self, arg):
        """
        Print all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            for obj in all_objs.values():
                print(obj)
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        else:
            for obj in all_objs.values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            else:
                obj = all_objs[key]
                attr_name = args[2]
                attr_type = type(getattr(obj, attr_name, ''))
                attr_value = attr_type(args[3].strip('"'))
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_all(self, arg):
        """
        Display string representations of all instances of a given class
        If no class is specified, displays all instantiated objects
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""

        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


def parse(arg):
    """
    Parse a string of arguments and return a list of tokens
    """
    tokens = []
    while arg:
        match = re.search(r'(\{.*?\}|\[.*?\])', arg)
        if match:
            start, end = match.span()
            tokens.extend(arg[:start].split())
            tokens.append(arg[start:end])
            arg = arg[end:]
        else:
            tokens.extend(arg.split())
            break
    return tokens


if __name__ == '__main__':
    HBNBCommand().cmdloop()
