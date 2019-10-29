Python Basics


Guido van Rossum in late 1980s designed and developed python programming language. Python is a high-level, open-source programming language. It is administered and maintained by Python Software Foundation.


Syntax
Python code can be written in any text editor. Python code file is saved with `*.py` file extension. Unlike many other programming languages, python uses indentation instead of braces `{}` to identify code blocks.

Identifier

The python code consists of set of instructions using different program element like variable, function, class, namespace, etc. The symbolic name of the program element like variable, function, class etc. is an `identifier`. Certain built-in identifiers are reserved and have specific meaning and uses.

```python
>>> import keyword
>>> keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
31
```

Identifier names are case-sensitive. Identifier names are alphanumeric and can only contain letter or underscore in the beginning of it. It cannot contain any special character. Reserved identifiers cannot be used as a name for any program element.

Variable

When we specifies the identifier for the program element, we are declaring the symbolic representation of the program element. When we specifies the data or value associated with the symbolic name of the program element, we are providing the definition for it.

Variable has the symbolic name which is used to refer to a memory location used by a computer program. This memory location would contain value or data. The value stored at this memory location is of specific type like numeric, string etc. The type of the value defines type of the data i.e. datatype of the variable.

Any program element can be identified by an identifier and hence assigned to a variable. The datatype of the variable in python is derived from the value being assigned to the variable (dynamically typed). This means that you do not need to declare the variables in python, and you can start using it by immediately assigning the value to it. It also ensures that the type of a variable can change during the execution of the python script. Once the value is assigned, it's datatype is locked and it can be treated and operated as that type alone (strongly typed) without explicitly converting it (typecasting).


Object Oriented Programming (OOP) Language

Object Oriented Programming (OOP) is one of the type of conceptual framework to classify programming languages among many others. Object Oriented Programming is based on the concept of 'objects' which can contain data values and methods. Objects are instances of classes. The classes are like a template which can be used to create any number of instances of that class and for any number of time. Every instance of a particular class is an independent entity. A class defines the 'type' of the instance of an object. Every instance of a particular class though considered independent will have the same 'type'.

In python, everything is an object which can to assigned to the variables and passed around. The 'type' of the data the variable stores defines the 'type' or 'datatype'.

https://www.techcluesblog.com/is-python-object-oriented-or-procedural/
https://en.wikipedia.org/wiki/Object-oriented_programming
https://en.wikipedia.org/wiki/Programming_paradigm
https://www.programiz.com/python-programming/class
https://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary
http://www.oznetnerd.com/python-everything-object-first-class-citizens/


Datatype

Different datatypes that the Python supports are following:
* Numbers - integer, long, float
* Boolean - True, False
* Strings 
* None - None
* list, tuple, dictionary, sets
* modules, classes, functions

```python
bool = True
name = "Craig"
age = 26
pi = 3.14159
print(name + ' is ' + str(age) + ' years old.')

# Scope
a = 1
b = 2
def Sum():
   global a, b
   b = a + b
Sum()
print(b)
```

https://www.programiz.com/python-programming/variables-datatypes
https://learning-python.readthedocs.io/en/latest/chapter03/README.html
https://www.programiz.com/python-programming/array

Statements and expression

Loosely defined, an 'expression' is a combination of variables, values, operators and literals which yields something, whereas 'statement' do something and are often composed of expressions (or other statements) and can span multiple lines.

https://docs.python.org/3/reference/expressions.html#is
https://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python

Some basic Python statements include:

print: Output strings, integers, or any other datatype.
The assignment statement: Assigns a value to a variable.
input: Allow the user to input numbers or booleans. WARNING: input accepts your input as a command and thus can be unsafe.
raw_input: Allow the user to input strings. If you want a number, you can use the int or float functions to convert from a string.
import: Import a module into Python. Can be used as import math and all functions in math can then be called by math.sin(1.57) or alternatively from math import sin and then the sine function can be called with sin(1.57).

Examples:

```python
print "Hello World"
print('Print works with or without parenthesis')
print("and single or double quotes")
print("Newlines can be escaped like\nthis.")
print("This text will be printed"),
print("on one line becaue of the comma.")
name = raw_input("Enter your name: ")
a = int(raw_input("Enter a number: "))
print(name + "'s number is " + str(a))
a = b = 5
a = a + 4
print a,b
9 5
```

Python expressions can include:
```python
a = b = 5 #The assignment statement
b += 1 #post-increment
c = "test"
import os,math #Import the os and math modules
from math import * #Imports all functions from the math module
```


```python
print "Hello World"
print('Print works with or without parenthesis')
print("and single or double quotes")
print("Newlines can be escaped like\nthis.")
print("This text will be printed"),
print("on one line becaue of the comma.")
```
* input
* raw_input
* The assignment statement: Assigns a value to a variable.
* import

```python
name = raw_input("Enter your name: ")
a = int(raw_input("Enter a number: "))
print(name + "'s number is " + str(a))
a = b = 5
a = a + 4
print a,b

a = b = 5 #The assignment statement
b += 1 #post-increment
c = "test"
import os,math #Import the os and math modules
from math import * #Imports all functions from the math module
```

Operators

* Arithmatic: `+, -, *, /, and % (modulus), // (modulus)`
* Comparison: `==, !=, <, >, <=, >=`
* Logical: `and, or, not`
* Exponentiation: `**`
* Execution: `os.system('ls -l') #Requires import os`

Maths

* Maths: Requires `import math`
* Absolute Value: `a = abs(-7.5)`
* Arc sine: `x = asin(0.5) #returns in rads`
* Ceil (round up): `print(ceil(4.2))`
* Cosine: `a = cos(x) #x in rads`
* Degrees: `a = degrees(asin(0.5)) #a=30`
* Exp: `y = exp(x) #y=e^x`
  - https://stackoverflow.com/questions/31951980/what-exactly-does-numpy-exp-do
  - The exponential function is e^x where e is a mathematical constant called Euler's number, approximately 2.718281. This value has a close mathematical relationship with pi and the slope of the curve e^x is equal to its value at every point. np.exp() calculates e^x for each value of x in your input array.
* Floor (round down): `a = floor(a+0.5)`
* Log: `x = log(y); #Natural Log`
   `x = log(y,5); #Base-5 log`
* Log Base 10: `x = log10(y)`
* Max: `mx = max(1, 7, 3, 4) #7`
   `mx = max(arr) #max value in array`
* Min: `mn = min(3, 0, -1, x) #min value`
* Powers: `x = pow(y,3) #x=y^3`
* Radians: `a = cos(radians(60)) #a=0.5`
* Random #: Random number functions require import random
   `random.seed() #Set the seed based on the system time.`
   `x = random() #Random number in the range [0.0, 1.0)`
   `y = randint(a,b) #Random integer in the range [a, b]`
* Round: `print round(3.793,1; #3.8 - rounded to 1 decimal`
   `a = round(3.793,0) #a=4.0`
* Sine: `a = sin(1.57) #in rads`
* Square Root: `x = sqrt(10) #3.16...`
* Tangent: `print tan(3.14)# #in rads`

Strings

List, Set, Tuple and Dictionary




Functions & Arguments


callables (say functions/classes).

Iterators

Variable Scope, Global Variables

Objects and Classes

Yes 1 is example of object of class int and 'sometext' is example of object of class str. They have own methods.

What might be confusing there is class named object which is parent class for all other classes. Function isinstance might be useful for learning about that:


https://stackoverflow.com/questions/4015417/python-class-inherits-object
https://docs.python.org/3/reference/datamodel.html#newstyle



Copy by reference, Copy by value

identity function id() 









There are some differences in this aspect from other programming languages on how the definition and declaration differs from that in the python for different program elements. Declaring a variable means binding it to a data type. Declaration of variables is not required in Python. If there is need of a variable, you think of a name and start using it as a variable. 




Operators


Documentation
pydoc -p 8080 


Built in Libraries
https://docs.python.org/3/library/index.html

Keyword
https://en.wikipedia.org/wiki/Reserved_word
https://www.programiz.com/python-programming/keyword-list


Compiled & Interpreted Language

High Level v/s Low Level Language

Strong & weak (loose) typing
https://en.wikipedia.org/wiki/Strong_and_weak_typing
dynamically typed languages (where type checking happens at run time) can also be strongly typed.

Definition & Declaration
https://techdifferences.com/difference-between-definition-and-declaration.html

https://www.python-course.eu/variables.php


object oriented programming &  procedure oriented programming
In procedure oriented programming the main emphasis is on functions
In object oriented programming stress on objects


Everything in Python is an Object

http://www.oznetnerd.com/python-everything-object-first-class-citizens/

https://medium.com/analytics-vidhya/why-should-you-know-in-python-everything-is-an-object-6a140c0b9293


https://stackoverflow.com/questions/865911/is-everything-an-object-in-python-like-ruby

https://medium.com/@larmalade/python-everything-is-an-object-and-some-objects-are-mutable-4f55eb2b468b

http://python-history.blogspot.com/2009/02/first-class-everything.html

https://gvanrossum.github.io//

http://neopythonic.blogspot.com
https://www.artima.com/weblogs/index.jsp?blogger=guido

