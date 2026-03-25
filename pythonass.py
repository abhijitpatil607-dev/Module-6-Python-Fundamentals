Introduction to Python

# 1. Introduction to Python and its Features

Python is a simple, high-level, and interpreted programming language. It is designed to be easy to read and write, making it beginner-friendly.

Features of Python:

Simple and easy to learn – Uses simple English-like syntax
High-level language – No need to manage memory manually
Interpreted – Code runs line by line, making debugging easier
Platform-independent – Runs on Windows, Linux, and Mac
Object-oriented – Supports classes and objects
Large library support – Has many built-in libraries for different tasks

2. History and Evolution of Python

Python was created by Guido van Rossum in the late 1980s and released in 1991.

Python 1.0 (1991): Basic features introduced
Python 2.0 (2000): Added new features like garbage collection
Python 3.0 (2008): Major improvements and better performance
Today, Python is widely used in web development, data science, AI, and automation.

3. Advantages of Python
Easy to learn and use
Readable syntax
Large community support
Cross-platform compatibility
Supports multiple programming styles (procedural, object-oriented)
Used in many fields like AI, machine learning, web development

4. Installing Python and Setting Up Environment

To start coding in Python, you need to install Python and a code editor.

Steps:

Go to the official website: https://www.python.org
Download and install Python
During installation, check “Add Python to PATH”
Install an IDE (Integrated Development Environment):
Anaconda – for data science
PyCharm – for professional coding
VS Code – lightweight and popular

# Write a Python program that prints "Hello, World!"
a = "Hello World"
print(a)

# Set up Python on your local machine and write a program to display your name.
a = "Hello i am aryan patil"
print(a)
===================================================================================
# 2. Programming Style


1. Understanding Python’s PEP 8 guidelines.
PEP 8 is a set of rules that tells how to write Python code in a proper and clean way. It helps programmers to keep their code neat and easy to understand.
For example, using proper spaces, not writing very long lines, and giving meaningful names to variables.

2.Indentation, comments, and naming conventions in Python.
Indentation means giving space at the beginning of a line. In Python, it is very important because it shows which code is inside a block. Usually, we use 4 spaces. If indentation is wrong, Python shows an error.
#CODE
if True:
    print("Hello")
*Comments
Comments are used to explain the code. They are not executed by Python.

Single-line comment uses #
Sometimes multi-line comments are also used

*Naming Conventions:
Names of variables and functions should be simple and easy to understand.

Examples:

total_marks
student_name

Class names are written differently, like StudentData.

*.Writing Readable and Maintainable Code

Readable code means code that is easy to understand. Maintainable code means code that can be easily changed later.

For this:

Use simple and clear names
Keep code short and clean
Write comments where needed
Avoid making code too complicated

# Write a Python program that demonstrates the correct use of indentation, comments, and variablesfollowing PEP 8 guidelines.
# This program calculates the total and average marks of a student

# taking input values
student_name = "Rahul"
marks_math = 80
marks_science = 75
marks_english = 85

# calculating total marks
total_marks = marks_math + marks_science + marks_english

# calculating average
average_marks = total_marks / 3

# displaying the result
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# checking result using indentation
if average_marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
========    ======================================================================
===============================================================================

# 3. Core Python Concepts

3.Understanding Data Types in Python

Data types tell what kind of value a variable stores.

Integer (int): Whole numbers
Example: 10, -5
Float (float): Decimal numbers
Example: 3.14, 2.5
String (str): Text data inside quotes
Example: "Hello"
List: Ordered collection, changeable
Example: [1, 2, 3]
Tuple: Ordered collection, not changeable
Example: (1, 2, 3)
Dictionary: Stores data in key-value pairs
Example: {"name": "Rahul", "age": 20}
Set: Unordered collection, no duplicate values
Example: {1, 2, 3}

1.Python variables and memory allocation.
 Variable :A variable is used to store data in Python.
 memory allocation :Python automatically assigns memory to variables when values are given. We don’t need to declare the data type separately. Memory is managed by Python itself, so it is easy for beginners.

3.Python operators: arithmetic, comparison, logical, bitwise?

1. Arithmetic Operators:         |2.Comparison Operators: |3.Logical Operators: | 4.Bitwise Operators:
Used for mathematical operations | == (Equal)             | and                 | & (AND)
+ (Addition)			 | != (Not equal)         | or                  | | (OR)
- (Subtraction)			 | > (Greater than)       | not                 | ^ (XOR)
* (Multiplication)		 | < (Less than)          |                     | ~ (NOT)
/ (Division)			 |                        |                     |
% (Modulus)	
# demonstrating different data types and variables

# integer
age = 20

# float
height = 5.7

# string
name = "Rahul"

# list
marks = [80, 75, 90]

# tuple
subjects = ("Math", "Science", "English")

# dictionary
student = {"name": "Rahul", "age": 20}

# set
unique_numbers = {1, 2, 3, 3}

# printing values
print(age)
print(height)
print(name)
print(marks)
print(subjects)
print(student)
print(unique_numbers)

=================================================================================
=================================================================================
# 4. 4.Conditional Statements
1.Introduction to conditionalstatements: if, else, elif?
 Conditional statements are used to make decisions in a program. They execute different code based on conditions.
if statement:
It checks a condition. If it is true, the code runs.
else statement:
It runs when the condition is false.
elif statement:
It is used to check multiple conditions.

2.Nested if-else conditions?
Nested if-else means using an if statement inside another if or else.
It is used when we need to check conditions inside another condition.



# 1.Practical Example 1: How does the Python code structure work?
x = 10

if x > 5:
    print("x is greater than 5")

print("Program ended")
==================================================================================
=================================================================================
# 2.How to create variables in Python?
a = 10          # integer
b = 3.5         # float
c = "Hello"     # string
==================================================================================
==================================================================================
#3.Practical Example 3: How to take user input using the input() function
# taking user input
name = input("Enter your name: ")

# printing the input
print("Hello", name)
=====================================================================================
================================================================================
# 4.Practical Example 4: How to check the type of a variable dynamically using type()
# creating variables
a = 10
b = 3.5
c = "Hello"

# checking types
print(type(a))
print(type(b))
print(type(c))
==================================================================================
==================================================================================
# Practical Example 5: Find Greater and Less Number using if-else
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number is:", a)
else:
    print("Greater number is:", b)
=============================================================================
=============================================================================
# Practical Example 6: Check if a Number is Prime
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")
================================================================================
===============================================================================
# Practical Example 7: Calculate Grades using if-else ladder
percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
else:
    print("Fail")
==============================================================================
==============================================================================
# Practical Example 8: Check Blood Donation Eligibility (Nested if)
age = int(input("Enter age: "))
weight = float(input("Enter weight: "))

if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible (weight should be at least 50 kg)")
else:
    print("Not eligible (age should be at least 18)")
================================================================================
===============================================================================
# 55. Looping (For, While)
Introduction to for and while Loops
Loops are used to repeat a block of code multiple times.
for loop:
It is used when we know how many times we want to run the loop.
while loop:
It runs as long as a condition is true.

How Loops Work in Python
Loops work by executing the same code again and again until a condition becomes false.
In a for loop, Python goes through each item in a sequence
In a while loop, Python checks the condition before every iteration
If the condition becomes false, the loop stops.

Using loops with collections (lists, tuples, etc.).
Loops can be used to go through items in collections like lists and tuples.
numbers = [1, 2, 3, 4]  ||  values = (10, 20, 30)
			||   
for num in numbers:	||    for v in values:
    print(num)          ||        print(v)



# Practical Example 1: Print each fruit using for loop
List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    print(fruit)
=================================================================================
===============================================================================
# Practical Example 2: Find length of each string in List1
List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    print(fruit, "length is", len(fruit))
    ===============================================================================
    ============================================================================
# Practical Example 3: Find a specific string using for loop and if condition
List1 = ['apple', 'banana', 'mango']

search = input("Enter fruit name: ")

for fruit in List1:
    if fruit == search:
        print("Found")
        break
else:
    print("Not Found")
=================================================================================
===============================================================================
List1 = ['apple', 'banana', 'mango']

search = input("Enter fruit name: ")

for fruit in List1:
    if fruit == search:
        print("Found")
        break
else:
    print("Not Found")
=============================================================================
============================================================================
# Practical Example 4: Print pattern using nested for loop
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()








