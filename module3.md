# Making decisions in Python

= is an assignment operator, e.g., a = b assigns a with the value of b;
== is the question are these values equal? so a == b compares a and b
Inequality: the not equal to operator (!=)
You can also ask a comparison question using the > (greater than) operator.

### If, else, elif

elif is used to check more than just one condition, and to stop when the first statement which is true is found.

zum Beispiel:
```bash
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
```

you mustn't use else without a preceding if;
else is always the last branch of the cascade, regardless of whether you've used elif or not;
else is an optional part of the cascade, and may be omitted;
if there is an else branch in the cascade, only one of all the branches is executed;
if there is no else branch, it's possible that none of the available branches is executed.

### Summary

1. The comparison (otherwise known as relational) operators are used to compare values. The table below illustrates how the comparison operators work, assuming that x = 0, y = 1, and z = 0:

![Questions](questions.png)

2. When you want to execute some code only if a certain condition is met, you can use a conditional statement:

- a single if statement, e.g.:

```bash
x = 10
 
if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.
```

- a series of if statements, e.g.:

```bash
x = 10
 
if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.
 
if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.
 
if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
``` 
Each if statement is tested separately.

- an if-else statement, e.g.:

```bash
x = 10
 
if x < 10: # condition
    print("x is less than 10")  # Executed if the condition is True.
 
else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.
```

- a series of if statements followed by an else, e.g.:

```bash
x = 10
 
if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.
 
if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.
 
if x == 10: # condition three
     print("x is equal to 10")  # Executed if condition three is True.
``` 
Each if is tested separately. The body of else is executed if the last if is False.

- The if-elif-else statement, e.g.:

```bash
x = 10
 
if x == 10: # True
    print("x == 10")
 
if x > 15: # False
    print("x > 15")
 
elif x > 10: # False
    print("x > 10")
 
elif x > 5: # True
    print("x > 5")
 
else:
    print("else will not be executed")
``` 

If the condition for if is False, the program checks the conditions of the subsequent elif blocks - the first elif block that is True is executed. If all the conditions are False, the else block will be executed.

- Nested conditional statements, e.g.:

```bash
x = 10
 
if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
```

## Loops

if you want to execute more than one statement inside one while loop, you must (as with if) indent all the instructions in the same way;
an instruction or set of instructions executed inside the while loop is called the loop's body;
if the condition is False (equal to zero) as early as when it is tested for the first time, the body is not executed even once (note the analogy of not having to do anything if there is nothing to do);
the body should be able to change the condition's value, because if the condition is True at the beginning, the body might run continuously to infinity – notice that doing a thing usually decreases the number of things to do).

The for loop is designed to do more complicated tasks – it can "browse" large collections of data item by item.

break – exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
continue – behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.

1. There are two types of loops in Python: while and for:

the while loop executes a statement or a set of statements as long as a specified boolean condition is true, e.g.:
```bash
# Example 1
while True:
    print("Stuck in an infinite loop.")
 
# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
```
the for loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set – you will learn about them soon) or other iterable objects (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function. Look at the examples below:

```bash
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")
 
# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
```

2. You can use the break and continue statements to change the flow of a loop:

You use break to exit a loop, e.g.:

```bash
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
```

You use continue to skip the current iteration, and continue with the next iteration, e.g.:

```bash
text = "pyxpyxpyx
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
```

3. The while and for loops can also have an else clause in Python. The else clause executes after the loop finishes its execution as long as it has not been terminated by break, e.g.:

```bash
n = 0
 
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
 
print()
 
for i in range(0, 3):
    print(i)
else:
    print(i, "else")
```

4. The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:

- start is an optional parameter specifying the starting number of the sequence (0 by default)
- stop is an optional parameter specifying the end of the sequence generated (it is not included),
- and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)

Example code:

```bash
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2
 
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
```

## Logic and bit operations in Python

One logical conjunction operator in Python is the word and. It's a binary operator with a priority that is lower than the one expressed by the comparison operators.
ZB: `counter > 0 and value == 100`

 A disjunction operator is the word or. It's a binary operator with a lower priority than and (just like + compared to *).

 In addition, there's another operator that can be applied to the construction of conditions. It's a unary operator performing a logical negation. Its operation is simple: it turns truth into falsehood and falsehood into truth.

This operator is written as the word not, and its priority is very high: the same as the unary + and -.

There are four operators that allow you to manipulate single bits of data. They are called bitwise operators.

& (ampersand) ‒ bitwise conjunction;
| (bar) ‒ bitwise disjunction;
~ (tilde) ‒ bitwise negation;
^ (caret) ‒ bitwise exclusive or (xor);

### Summary

1. Python supports the following logical operators:

and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.

2. You can use bitwise operators to manipulate single bits of data. The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

`&` does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
`|` does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
`˜`  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
`^` does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
`>>` does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
`<<` does a bitwise left shift, e.g., y << 3 = 128, which is 1000 0000 in binary.
`*` -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.

## Lists

### len()
The function takes the list's name as an argument, and returns the number of elements currently stored inside the list (in other words ‒ the list's length).

### del
Any of the list's elements may be removed at any time ‒ this is done with an instruction named del (delete). Note: it's an instruction, not a function.

### Functions vs methods
A method is owned by the data it works for, while a function is owned by the whole code.

In general, a typical function invocation may look like this:
`result = function(arg)`

A typical method invocation usually looks like this:
`result = data.method(arg)`

The method will behave like a function, but can do something more ‒ it can change the internal state of the data from which it has been invoked.

### append()
Such an operation is performed by a method named append(). It takes its argument's value and puts it at the end of the list which owns the method.
`list.append(value)`

### insert ()
The insert() method is a bit smarter ‒ it can add a new element at any place in the list, not only at the end.
`list.insert(location, value)`

### Sumary

1. The list is a type of data in Python used to store multiple objects. It is an ordered and mutable collection of comma-separated items between square brackets, e.g.:
```bash
my_list = [1, None, True, "I am a string", 256, 0]
```

2. Lists can be indexed and updated, e.g.:
```bash
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0
 
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
 
my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
```

3. Lists can be nested, e.g.:
```bash
my_list = [1, 'a', ["list", 64, [0, 1], False]]
```

You will learn more about nesting in module {{_moduleNumber}}.7 ‒ for the time being, we just want you to be aware that something like this is possible, too.

4. List elements and lists can be deleted, e.g.:
```bash
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]
 
del my_list  # deletes the whole list
```

Again, you will learn more about this in module {{_moduleNumber}}.6 ‒ don't worry. For the time being just try to experiment with the above code and check how changing it affects the output.

5. Lists can be iterated through using the for loop, e.g.:
```bash
my_list = ["white", "purple", "blue", "yellow", "green"]
 
for color in my_list:
    print(color)
```

6. The len() function may be used to check the list's length, e.g.:
```bash
my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5
 
del my_list[2]
print(len(my_list))  # outputs 4
```

7. A typical function invocation looks as follows: result = function(arg), while a typical method invocation looks like this:result = data.method(arg).

## The bubble sort algorithm

sorting a list in python:
```bash
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
```

### Summary

1. You can use the sort() method to sort elements of a list, e.g.:
```bash
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]
```

2. There is also a list method called reverse(), which you can use to reverse the list, e.g.:
```bash
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]
```

## Operations on lists

### Slice
`start` is the index of the first element included in the slice;
`end` is the index of the first element not included in the slice.

### Summary

1. If you have a list list_1, then the following assignment: list_2 = list_1 does not make a copy of the list_1 list, but makes the variables list_1 and list_2 point to one and the same list in memory. For example:
```bash
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']
```

2. If you want to copy a list or part of the list, you can do it by performing slicing:
```bash
colors = ['red', 'green', 'orange']
 
copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list
```

3. You can use negative indices to perform slices, too. For example:
```bash
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
```

4. The start and end parameters are optional when performing a slice: list[start:end], e.g.:
```bash
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
```

5. You can delete slices using the del instruction:
```bash
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]
 
del my_list[:]
print(my_list)  # deletes the list content, outputs: []
```

6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:
```bash
my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False
```

## Lists in advanced applications

### Summary

1. List comprehension allows you to create new lists from existing ones in a concise and elegant way. The syntax of a list comprehension looks as follows:

[expression for element in list if conditional]
 
which is actually an equivalent of the following code:
```bash
for element in list:
    if conditional:
        expression
```
Here's an example of a list comprehension ‒ the code creates a five-element list filled with the first five natural numbers raised to the power of 3:
```bash
cubed = [num ** 3 for num in range(5)]
print(cubed) # outputs: [0, 1, 8, 27, 64]
```

2. You can use nested lists in Python to create matrices (i.e., two-dimensional lists). For example:

```bash
# A four-column/four-row table ‒ a two dimensional array (4x4)
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'
```

3. You can nest as many lists in lists as you want, thereby creating n-dimensional lists, e.g., three-, four- or even sixty-four-dimensional arrays. For example:
```bash
# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
```
