# The AirBnB Clone Project
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## AirBnB Clone Console
Welcome to the AirBnB Clone Console! This is the first step towards building the AirBnB clone project, a full web application that mimics some functionalities of the popular accommodation rental platform, Airbnb.

## Overview
The AirBnB Clone Console is a Python-based command-line interface (CLI) that allows you to manage AirBnB objects, such as users, states, cities, places, and more. With this console, you can perform various operations on these objects, including creating, retrieving, updating, and deleting them.

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the following actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Performing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

## - Getting Started:

## * Prerequisites
-   Python 3.8.5 or higher

## * How to start it
These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

## - Installation:
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

1.  Clone this GitHub repository to your local machine:
```
git clone https://github.com/amilemia/AirBnB_clone
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work:

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
> models/state.py: State class that inherits from BaseModel
>
> models/city.py: City class that inherits from BaseModel
>
> models/amenity.py: Amenity class that inherits from BaseModel
>
> models/place.py: Place class that inherits from BaseModel
>
> models/review.py: Review class that inherits from BaseModel

2.  Navigate to the project directory:

```
cd AirBnB-Clone
```

3.  Execute the console:

```
./console.py
```

## - Usage:

The console provides a set of commands to interact with the AirBnB objects. Here are some of the available commands:

-   `help`: Display a list of documented commands and their descriptions.
-   `quit`: Exit the console.

Please refer to the AirBnB concept page for more details on the supported objects and their functionalities.

## - Examples:

### Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## * Running Tests

To ensure the proper functionality of the console, run the unit tests using the following command:

`python3 -m unittest discover tests` 

## - Learning Objectives:

-   Understand how to create a Python package.
-   Build a command interpreter in Python using the `cmd` module.
-   Implement Unit testing in a large project.
-   Serialize and deserialize a class.
-   Read and write JSON files.
-   Handle datetime objects.
-   Use UUIDs for unique identifiers.
-   Utilize `*args` and `**kwargs` for handling variable arguments.

## - Authors:

-   [ITRI M'BARKI](https://github.com/amasin76)
-   [Mohammed-Amine Madah](https://github.com/amilemia)
