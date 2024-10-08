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

# Returning a result from a function

![return](return.png)

## None
None is a keyword.

There are only two kinds of circumstances when None can be safely used:

- when you assign it to a variable (or return it as a function's result)
- when you compare it with a variable to diagnose its internal state.

## Summary

1. You can use the return keyword to tell a function to return some value. The return statement exits the function, e.g.:
```bash
def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # outputs: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # outputs: None
```

2. The result of a function can be easily assigned to a variable, e.g.:
```bash
def wishes():
    return "Happy Birthday!"
 
w = wishes()
 
print(w) # outputs: Happy Birthday!
```
Look at the difference in output in the following two examples:
```bash
# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"
 
wishes() # outputs: My Wishes
 
 
# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"
 
print(wishes())
 
# outputs: My Wishes
# Happy Birthday
```

3. You can use a list as a function's argument, e.g.:
```bash
def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)
 
hi_everybody(["Adam", "John", "Lucy"])
```

4. A list can be a function result, too, e.g.:
```bash
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(create_list(5))
```

# Scope in Python

A variable existing outside a function has scope inside the function's body, excluding those which define a variable of the same name.

It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). Assigning a value forces the creation of the function's own variable.

## global

There's a special Python method which can extend a variable's scope in a way which includes the function's body (even if you want not only to read the values, but also to modify them).

zb: 
```bash
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
```

The output will be:
```bash
Do I know that variable? 2
2
```

## Summary

1. A variable that exists outside a function has scope inside the function body (Example 1) unless the function defines a variable of the same name (Example 2, and Example 3), e.g.:

Example 1:
```bash
var = 2
 
 
def mult_by_var(x):
    return x * var
 
 
print(mult_by_var(7)) # outputs: 14
```

Example 2:
```bash
def mult(x):
    var = 5
    return x * var
 
 
print(mult(7)) # outputs: 35
```

Example 3:
```bash
def mult(x):
    var = 7
    return x * var
 
 
var = 3
print(mult(7)) # outputs: 49
```

2. A variable that exists inside a function has scope inside the function body (Example 4), e.g.:

Example 4:
```bash
def adding(x):
    var = 7
    return x + var
 
 
print(adding(4)) # outputs: 11
print(var) # NameError
```

3. You can use the global keyword followed by a variable name to make the variable's scope global, e.g.:
```bash
var = 2
print(var) # outputs: 2
 
 
def return_var():
    global var
    var = 5
    return var
 
 
print(return_var()) # outputs: 5
print(var) # outputs: 5
```

# Creating multi-parameter functions

## Summary

1. A function can call other functions, or even itself. When a function calls itself, this situation is known as recursion, and the function which calls itself and contains a specified termination condition (i.e., the base case − a condition which doesn't tell the function to make any further calls to that function) is called a recursive function.

2. You can use recursive functions in Python to write clean, elegant code, and divide it into smaller, organized chunks. On the other hand, you need to be very careful as it might be easy to make a mistake and create a function which never terminates. You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient.

When using recursion, you need to take all its advantages and disadvantages into consideration.

The factorial function is a classic example of how the concept of recursion can be put in practice:
```bash
# Recursive implementation of the factorial function.
 
def factorial(n):
    if n == 1: # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24
```

# Tuples and dictionaries

## Tuples

tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.

Look at the example:
```bash
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
```

What else can tuples do for you?

- the len() function accepts tuples, and returns the number of elements contained inside;
- the + operator can join tuples together (we've shown you this already)
- the * operator can multiply tuples, just like lists;
- the in and not in operators work in the same way as in lists.

## Dictionaries

- each key must be unique − it's not possible to have more than one key of the same value;
- a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
- a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
- the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
- a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.

Example:
```bash
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary['cat'])
print(phone_numbers['Suzy'])
```

Console:
```bash
chat
22657854310
```

## Summary Tuples

1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:
```bash
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)
 
Each tuple element may be of a different type (i.e., integers, strings, booleans, etc.). What is more, tuples can contain other tuples or lists (and the other way round).
```

2. You can create an empty tuple like this:
```bash
empty_tuple = ()
print(type(empty_tuple)) # outputs: <class 'tuple'>
```

3. A one-element tuple may be created as follows:
```bash
one_elem_tuple_1 = ("one", ) # Brackets and a comma.
one_elem_tuple_2 = "one", # No brackets, just a comma.
```

If you remove the comma, you will tell Python to create a variable, not a tuple:
```bash
my_tuple_1 = 1,
print(type(my_tuple_1)) # outputs: <class 'tuple'>
 
my_tuple_2 = 1 # This is not a tuple.
print(type(my_tuple_2)) # outputs: <class 'int'>
```

4. You can access tuple elements by indexing them:
```bash
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3]) # outputs: [3, 4]
```

5. Tuples are immutable, which means you cannot change their elements (you cannot append tuples, or modify, or remove tuple elements). The following snippet will cause an exception:
```bash
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar" # The TypeError exception will be raised.
```

However, you can delete a tuple as a whole:
```bash
my_tuple = 1, 2, 3,
del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined
```

6. You can loop through a tuple elements (Example 1), check if a specific element is (not)present in a tuple (Example 2), use the len() function to check how many elements there are in a tuple (Example 3), or even join/multiply tuples (Example 4):
```bash
# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
 
# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
 
# Example 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)
# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
 
print(tuple_4)
print(tuple_5)
```

EXTRA  
You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:
```bash
my_tuple = tuple((1, 2, "string"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # outputs: [2, 4, 6]
print(type(my_list)) # outputs: <class 'list'>
tup = tuple(my_list)
print(tup) # outputs: (2, 4, 6)
print(type(tup)) # outputs: <class 'tuple'>
```

By the same fashion, when you want to convert an iterable to a list, you can use a Python built-in function called list():
```bash
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # outputs: <class 'list'>
```

## Summary Dictionaries
1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data. (*Since Python 3.6x dictionaries have become ordered by default.)

Each dictionary is a set of key: value pairs. You can create it by using the following syntax:
```bash
my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}
```

2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the get() method (ex. 2):
```bash
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }
 
item_1 = pol_eng_dictionary["gleba"] # ex. 1
print(item_1) # outputs: soil
 
item_2 = pol_eng_dictionary.get("woda") # ex. 2
print(item_2) # outputs: water
```

3. If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:
```bash
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]
print(item) # outputs: lock
```

4. To add or remove a key (and the associated value), use the following syntax:

```bash
phonebook = {} # an empty dictionary
 
phonebook["Adam"] = 3456783958 # create/add a key-value pair
print(phonebook) # outputs: {'Adam': 3456783958}
 
del phonebook["Adam"]
print(phonebook) # outputs: {}
```

You can also insert an item into a dictionary by using the update() method, and remove the last element by using the popitem() method, e.g.:

```bash
pol_eng_dictionary = {"kwiat": "flower"}
 
pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}
 
pol_eng_dictionary.popitem()
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'}
```

5. You can use the for loop to loop through a dictionary, e.g.:

```bash
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
for item in pol_eng_dictionary:
    print(item)
 
#          woda
#          gleba
```

6. If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:

```bash
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)
```

7. To check if a given key exists in a dictionary, you can use the in keyword:

```bash
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
if "zamek" in pol_eng_dictionary:
   print("Yes")
else:
   print("No")
```

8. You can use the del keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the clear() method:

```bash
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
print(len(pol_eng_dictionary)) # outputs: 3
del pol_eng_dictionary["zamek"] # remove an item
print(len(pol_eng_dictionary)) # outputs: 2
 
pol_eng_dictionary.clear() # removes all the items
print(len(pol_eng_dictionary)) # outputs: 0
 
del pol_eng_dictionary # removes the dictionary
```

9. To copy a dictionary, use the copy() method:

```bash
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"}
 
copy_dictionary = pol_eng_dictionary.copy()
```

# Exceptions

## Summary
1. In Python, there is a distinction between two kinds of errors:

- syntax errors (parsing errors), which occur when the parser comes across a statement that is incorrect. For example:
Trying to execute the following line:
```bash
print("Hello, World!)
```

will cause a SyntaxError, and result in the following (or similar) message being displayed in the console:

Pay attention to the arrow – it indicates the place where the Python parser has run into trouble. In our case, it's the missing double quote. Did you notice it?
```bash
File "main.py", line 1
 
    print("Hello, World!)
                        ^
SyntaxError: EOL while scanning string literal
```

exceptions, which occur even when a statement/expression is syntactically correct; these are the errors that are detected during execution when your code results in an error which is not uncoditionally fatal. For example:
Trying to execute the following line:
```bash
print(1/0)
```

will cause a ZeroDivisionError exception, and result in the following (or similar) message being displayed in the console:
```bash
Traceback (most recent call last):
  File "main.py", line 1, in
    print(1/0)
ZeroDivisionError: division by zero
```

Pay attention to the last line of the error message – it actually tells you what happened. There are many different types of exceptions, such as ZeroDivisionError, NameError, TypeError, and many more; and this part of the message informs you of what type of exception has been raised. The preceding lines show you the context in which the exception has occured.

2. You can "catch" and handle exceptions in Python by using the try-except block. So, if you have a suspicion that any particular snippet may raise an exception, you can write the code that will gracefully handle it, and will not interrupt the program. Look at the example:
```bash
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")
```

The code above asks the user for input until they enter a valid integer number. If the user enters a value that cannot be converted to an int, the program will print Warning: the value entered is not a valid number. Try again..., and ask the user to enter a number again. What happens in such a case?

1. The program enters the while loop.
2. The try block/clause is executed. The user enters a wrong value, for example: hello!.
3. An exception occurs, and the rest of the try clause is skipped. The program jumps to the except block, executes it, and then continues running after the     try-except block.

If the user enters a correct value and no exception occurs, the subsequent instructions in the try block are executed.

3. You can handle multiple exceptions in your code block. Look at the following examples:
```bash
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")
```

You can use multiple except blocks within one try statement, and specify particular exception names. If one of the except branches is executed, the other branches will be skipped. Remember: you can specify a particular built-in exception only once. Also, don't forget that the default (or generic) exception, that is the one with no name specified, should be placed at the bottom of the branch (use the more specific exceptions first, and the more general last).

You can also specify and handle multiple built-in exceptions within a single except clause:
```bash
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")
```

4. Some of the most useful Python built-in exceptions are: ZeroDivisionError, ValueError, TypeError, AttributeError, and SyntaxError. One more exception that, in our opinion, deserves your attention is the KeyboardInterrupt exception, which is raised when the user hits the interrupt key (CTRL-C or Delete). Run the code above and hit the key combination to see what happens.

To learn more about the Python built-in exceptions, consult the official Python documentation.

5. Last but not least, you should remember about testing and debugging your code. Use such debugging techniques as print debugging; if possible – ask someone to read your code and help you to find bugs in it or to improve it; try to isolate the fragment of code that is problematic and susceptible to errors: test your functions by applying predictable argument values, and try to handle the situations when someone enters wrong values; comment out the parts of the code that obscure the issue. Finally, take breaks and come back to your code after some time with a fresh pair of eyes.
