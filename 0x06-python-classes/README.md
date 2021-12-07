# 0x06. Python - Classes and Objects

## Background Context
OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

## Resources
Read or watch:
* [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, ``classmethod`` and ``staticmethod`` yet)
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, ``The __init__`` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

## General
* Why Python programming is awesome
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is ``self``
* What is a method
* What is the special ``__init__`` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the ``__dict__`` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the ``getattr`` function

# Requirements

## General
* Allowed editors: ``vi, vim, emacs``
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly ``#!/usr/bin/python3``
* A ``README.md`` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using ``wc``
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__))
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# More Info
Documentation is now mandatory! Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

# Quiz questions

## Question #0
In this following code, what is User?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
Options
* A class
* A string
* An attribute
* A method
* An instance
Correct Option
* A class

## Question #1
In this following code, what is id?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
Options
* A public instance attribute
* A public class attribute
* A public class method
* A pulic instance method
* A private class attribute
* A protected class attribute
Correct Option
* A public class attribute

## Question #2
In this following code, what is __password?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
Options
* A public class attribute
* A public instance attribute
* A protected class attribute
* A proctected class attribute
* A private class attribute
* A provate instance attribute
Correct Option
* A private class attribute

## Question #3
In this following code, what is is_new?
```
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
Options
* A public class attribute
* A public instance attribute
* A protected class attribute
* A proctected instance attribute
* A private class attribute
* A provate instance attribute
Correct Option
* A public instance attribute

## Question #4
What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new
```
Options
* is_new
* Nothing
* False
* True
Correct Option
* True

## Question #5
What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.id
```
Options
* 89
* id
* User.id
* Nothing
Correct Option
* 89

## Question #6
What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User("John")
>>> u.name
```
Options
* name
* None
* John
* no name
Correct Option
* John

## Question #7
What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name
```
Options
* name
* None
* John
* no name
Correct Option
* no name
