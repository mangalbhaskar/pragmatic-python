# How to Get Started With Python?

Python programming language can run on different playforms like Linux, Windows, MacOS, IoT devies, Android.


Cloud based REPL Interface

You can immediately get started writing python code using an interactive cloud based programming interfaces. One such cloud based interface is [repl.it/languages/Python3](https://repl.it/languages/Python3).

You will need to install Python if you want to code and run on your computer. It's always good to install the latest but the most stable version of python on your computer. The defacto, pre-installed python on the operating system may be out-of-date.

Python IDE for Begginers

If you want to start coding quickly in less then 5 mins without much hassel of choosing python version, system configuration, you can install Thonny IDE (Interactive Development Evnironment). Thonny IDE provides with latest version of Python. An IDE provide the GUI based set of tools like source code editor, interactive shell and a debugger. IDE provides useful features like code hinting, syntax highlighting and checking, file explorers etc. and can make your life easier, but beware of adopting it completely in the begging stages as you may become handicapped without IDE if you have not learned how to code in using a simple text editor, execute and debug it form the commmand line.

Thonny IDE is one of the most intutive, simple and with clean interface Python IDE for beginners.

1. Download Thonny IDE and run the installer to install it on your computer.
2. Go to File > New. Then save the file with .py extension. For example, hello.py, example.py etc.
3. You can give any name to the file. However, the file name should end with .py
4. Write Python code in the file and save it.
5. Then Go to Run > Run current script or simply click F5 to run it.


Use the defacto pre-installed Python on your operating system



Install Python Separately

The Python IDE will help get started quickly, help you to learn python syntax and assist in quick debugging. Inspite of the immediate benefit you forsee, my strong advice to the begginers is to take some time to install, configure python separately, use text editor to write your code and run it from the command line. This may be daunting initially but will have long term benefits on honing your skills in writing good quality code without depending on the IDE to assist you in each step. Learn to use and get comfortable with command line interface.

1. Download the latest version of Python, run the installer file, and follow the steps to install Python
2. During the install process, check Add Python to environment variables. This will add Python to environment variables and you are able to run Python from any part of the computer.
3. Once you finish the installation process, you can run Python.

Once Python is installed, typing python in the command line will invoke the interpreter in immediate mode. We can directly type in Python code and press enter to get the output.



https://www.programiz.com/python-programming/first-program
https://www.python.org/downloads/
https://thonny.org/

sudo apt install thonny


read–eval–print-loop (REPL)
https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
https://repl.it/languages/Python3

https://en.wikipedia.org/wiki/Integrated_development_environment

## Hello World!
















```python
# 1.py
print("Hello World!")
```

```python
# 2.py
message = "Hello World!"
print(message)
```


```python
>>> import keyword
>>> keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
31
```


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

