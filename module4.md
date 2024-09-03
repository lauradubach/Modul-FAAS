# Functions

This is what the simplest function definition looks like:
```bash
def function_name():
    function_body
```

![function](function.png)

## Summary

1. A function is a block of code that performs a specific task when the function is called (invoked). You can use functions to make your code reusable, better organized, and more readable. Functions can have parameters and return values.

2. There are at least four basic types of functions in Python:

- built-in functions which are an integral part of Python (such as the print() function). You can see a complete list of built-in Python functions at https://docs.python.org/3/library/functions.html.
- the ones that come from pre-installed modules (you'll learn about them in the Python Essentials 2 course)
- user-defined functions which are written by users for users ‒ you can write your own functions and use them freely in your code,
- the lambda functions (you'll learn about them in the Python Essentials 2 course.)

3. You can define your own function using the def keyword and the following syntax:
```bash
def your_function(optional parameters):
    # the body of the function
```

You can define a function which doesn't take any arguments, e.g.:
```bash
def message(): # defining a function
    print("Hello") # body of the function
 
message() # calling the function
```

You can define a function which takes arguments, too, just like the one-parameter function below:
```bash
def hello(name): # defining a function
    print("Hello,", name) # body of the function
 
 
name = input("Enter your name: ")
 
hello(name) # calling the function
```

# How functions communicate with their environment

Don't forget:

parameters live inside functions (this is their natural environment)
arguments exist outside functions, and are carriers of values passed to corresponding parameters.

Let's implement that social custom in Python. The following function will be responsible for introducing somebody:
```bash
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
```
## summary

1. You can pass information to functions by using parameters. Your functions can have as many parameters as you need.

An example of a one-parameter function:
```bash
def hi(name):
    print("Hi,", name)
 
hi("Greg")
 ```

An example of a two-parameter function:
```bash
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)
 
hi_all("Sebastian", "Konrad")
```

An example of a three-parameter function:
```bash
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
 
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)
```

2. You can pass arguments to a function using the following techniques:

- positional argument passing in which the order of arguments passed matters (Ex. 1)
- keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2)
- a mix of positional and keyword argument passing (Ex. 3.)
```bash
Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # outputs: 3
subtra(2, 5) # outputs: -3
 
 
Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # outputs: 3
subtra(b=2, a=5) # outputs: 3
 
Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(5, 2) # outputs: 3
```

It's important to remember that positional arguments mustn't follow keyword arguments. That's why if you try to run the following snippet:
```bash
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(a=5, 2) # Syntax Error
```

Python will not let you do it by signalling a SyntaxError.

3. You can use the keyword argument-passing technique to pre-define a value for a given argument:
```bash
def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # outputs: Andy Smith
name("Betty", "Johnson") # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
```
