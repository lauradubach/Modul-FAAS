# Start with Python

**alphabetically** – a program needs to be written in a recognizable script, such as Roman, Cyrillic, etc.
**lexically** – each programming language has its dictionary and you need to master it; thankfully, it's much simpler and smaller than the dictionary of any natural language;
**syntactically** – each language has its rules and they must be obeyed;
**semantically** – the program has to make sense.

![compliationvsinterpretation](compliationvsinterpretation.png)

![vergleich](vergleich.png)

Python is an interpreted language. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.
If you want to program in Python, you'll need the Python interpreter. You won't be able to run your code without it. Fortunately, Python is free. This is one of its most important advantages.

## What is Python?

Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.

And while you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python's Flying Circus.

At the height of its success, the Monty Python team were performing their sketches to live audiences across the world, including at the Hollywood Bowl.

Since Monty Python is considered one of the two fundamental nutrients to a programmer (the other being pizza), Python's creator named the language in honor of the TV show.

## Despite Python's growing popularity, there are still some niches where Python is absent, or is rarely seen:

low-level programming (sometimes called "close to metal" programming): if you want to implement an extremely effective driver or graphical engine, you wouldn't use Python;
applications for mobile devices: although this territory is still waiting to be conquered by Python, it will most likely happen someday.


| Befehl | Funktion |
| ---- | ---- |
| `print("Hello, world!")` | etwas schreiben |
| `\n`| neue output linie in einem print setzten, zb; `print("The itsy bitsy spider\nclimbed up the waterspout.")` |
| `print("The itsy bitsy spider" , "climbed up" , "the waterspout.")` | mit kommas mehrere argumente nacheinander machen |
| `print("My", "name", "is", "Monty", "Python.", sep="-")` | keyword verwenden, hier im beispiel sep="-". Es wird zwischen den zeilen überall "-" ausgegeben, so wird es dann ausgegeben: My-name-is-Monty-Python. |
|`end="*"`| keyword end, wird am ende des satzes verwendet und angegeben |

1. Literals are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").

2. The binary system is a system of numbers that employs 2 as the base. Therefore, a binary number is made up of 0s and 1s only, e.g., 1010 is 10 in decimal.

Octal and hexadecimal numeration systems, similarly, employ 8 and 16 as their bases respectively. The hexadecimal system uses the decimal numbers and six extra letters.
3. Integers (or simply ints) are one of the numerical types supported by Python. They are numbers written without a fractional component, e.g., 256, or -1 (negative integers).

4. Floating-point numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers that contain (or are able to contain) a fractional component, e.g., 1.27.

5. To encode an apostrophe or a quote inside a string, you can either use the escape character, e.g., 'I\'m happy.', or open and close the string using an opposite set of symbols to the ones you wish to encode, e.g., "I'm happy." to encode an apostrophe, and 'He said "Python", not "typhoon"' to encode a (double) quote.

6. Boolean values are the two constant objects True and False used to represent truth values (in numeric contexts 1 is True, while 0 is False.

## Python Literals

You use literals to encode data and to put them into your code.

Zusammenrechnen von zahlen kann man so ausschreiben:
```bash
print(0x123)
```
Hier braucht es keine "", da der computer zahlen lesen kann.

Grösser und kleinder als verwenden: 
```bash
print(True > False)
print(True < False)
```
Die ausgabe sollte nun wie folgt aussehen:

```bash
True
False
```

What types of literals are the following four examples?

"1.5", 2.0, 528, False

The first is a string, the second is a numerical literal (a float), the third is a numerical literal (an integer), and the fourth is a boolean literal.

## Basic Python operators

+
-
*
/
//
%
**

Key takeaways
1. An expression is a combination of values (or variables, operators, calls to functions ‒ you will learn about them soon) which evaluates to a certain value, e.g., 1 + 2.

2. Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the * operator multiplies two values: x * y.

3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division ‒ always returns a float), % (modulus ‒ divides left operand by right operand and returns the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation ‒ left operand raised to the power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division ‒ returns a number resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)

4. A unary operator is an operator with only one operand, e.g., -1, or +3.

5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

6. Some operators act before others - the hierarchy of priorities:

the ** operator (exponentiation) has the highest priority;
then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example 4 ** -1 equals 0.25)
then: *, /, and %,
and finally, the lowest priority: binary + and -.

7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.