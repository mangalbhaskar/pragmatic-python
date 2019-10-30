# Python Basics


Guido van Rossum in late 1980s designed and developed python programming language. Python is a high-level, open-source programming language. It is administered and maintained by Python Software Foundation.


## Syntax

Python code can be written in any text editor. Python code file is saved with `*.py` file extension. Unlike many other programming languages, python uses indentation instead of braces `{}` to identify code blocks.

* Indentation
* Comments

## Identifier

The python code consists of set of instructions using different program element like variable, function, class, namespace, etc. The symbolic name of the program element like variable, function, class etc. is an `identifier`. Certain built-in identifiers are reserved and have specific meaning and uses.

Identifier names are case-sensitive. Identifier names are alphanumeric and can only contain letter or underscore in the beginning of it. It cannot contain any special character. Reserved identifiers cannot be used as a name for any program element.


## Variable

When we specifies the identifier for the program element, we are declaring the symbolic representation of the program element. When we specifies the data or value associated with the symbolic name of the program element, we are providing the definition for it.

Variable has the symbolic name which is used to refer to a memory location used by a computer program. This memory location would contain value or data. The value stored at this memory location is of specific type like numeric, string etc. The type of the value defines type of the data i.e. datatype of the variable.

Any program element can be identified by an identifier and hence assigned to a variable. The datatype of the variable in python is derived from the value being assigned to the variable (dynamically typed). This means that you do not need to declare the variables in python, and you can start using it by immediately assigning the value to it. It also ensures that the type of a variable can change during the execution of the python script. Once the value is assigned, it's datatype is locked and it can be treated and operated as that type alone (strongly typed) without explicitly converting it (typecasting).


## Object Oriented Programming (OOP) Language

Object Oriented Programming (OOP) is one of the type of conceptual framework to classify programming languages among many others. Object Oriented Programming is based on the concept of 'objects' which can contain data values and methods. Objects are instances of classes. The classes are like a template which can be used to create any number of instances of that class and for any number of time. Every instance of a particular class is an independent entity. A class defines the 'type' of the instance of an object. Every instance of a particular class though considered independent will have the same 'type'.

In python, everything is an object which can to assigned to the variables and passed around. The 'type' of the data the variable stores defines the 'type' or 'datatype'.


## Datatype

Different datatypes that the Python supports are following:
* Numbers - integer, long, float
* Boolean - True, False
* Strings 
* None - None
* list, tuple, dictionary, sets
* modules, classes, functions


## Statements and expression

Loosely defined, an 'expression' is a combination of variables, values, operators and literals which yields something, whereas 'statement' do something and are often composed of expressions (or other statements) and can span multiple lines.

Some basic Python statements include:
* print: Output strings, integers, or any other datatype
* The assignment statement: Assigns a value to a variable
* input: Allow the user to input numbers or booleans. WARNING: input accepts your input as a command and thus can be unsafe.
* raw_input: Allow the user to input strings. If you want a number, you can use the int or float functions to convert from a string.
* import: Import a module into Python. Can be used as import math and all functions in math can then be called by math.sin(1.57) or alternatively from math import sin and then the sine function can be called with sin(1.57).


## Operators

In general, the programming construct that perform an operation on values and variables are opertators. Broadly there are seven differet categories in which operators can be classified into.
* Assignment operators: `=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=`
* Arithmatic operators: `+ (addition), - (subtraction), * (multiplication), / (division), and % (modulus), // (floor division), ** (Exponentiation)`
* Comparison operators: `==, !=, <, >, <=, >=`
* Logical operators: `and, or, not`
* Identity operators: `is, is not`
* Membership operators: `in, not in`
* Bitwise operators: `& (and), | (or), ^ (xor), ~ (not), << (left shift), >> (right shift)`
* Execution: `os.system('ls -l') #Requires import os`


## References

Object Oriented Programming (OOP) Language
* https://www.techcluesblog.com/is-python-object-oriented-or-procedural/
* https://en.wikipedia.org/wiki/Object-oriented_programming
* https://en.wikipedia.org/wiki/Programming_paradigm
* https://www.programiz.com/python-programming/class
* https://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary
* http://www.oznetnerd.com/python-everything-object-first-class-citizens/

Datatype
* https://www.programiz.com/python-programming/variables-datatypes
* https://learning-python.readthedocs.io/en/latest/chapter03/README.html
* https://www.programiz.com/python-programming/array

Statements and expression
* https://docs.python.org/3/reference/expressions.html#is
* https://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python

Operators
* https://www.learnbyexample.org/python-operators/
