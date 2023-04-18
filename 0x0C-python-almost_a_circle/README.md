0x0C. Python - Almost a circle
This project is part of the Higher Level Programming curriculum at ALX School. It covers the following topics:

Import
Exceptions
Class
Private attribute
Getter/Setter
Class method
Static method
Inheritance
Unittest
Read/Write file
args and kwargs
Serialization/Deserialization
JSON
The goal of this project is to create a class hierarchy for simple geometric shapes, starting with a base class called Base and adding more specific classes like Rectangle, Square, and Circle that inherit from Base. Each shape will have its own implementation of methods like area() and display(), and the classes will be able to be serialized and deserialized to and from JSON.

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*) style
All your files must be executable
The length of your files will be tested using wc
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start with test_
Your file organization in the tests folder should be the same as your project: for example, for models/base.py, unit tests must be in tests/test_models/test_base.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
We strongly encourage you to work together on test cases so that you don't miss any edge case
Files
models/
This directory contains the classes that represent geometric shapes.

tests/
This directory contains unit tests for the classes in the models/ directory.

AUTHORS
This file contains the authors of the project.

README.md
This file contains information about the project and how to use it.

Tasks
0. If it's not tested it doesn't work
All your files, classes, and methods must be unit tested and be PEP 8 validated.

