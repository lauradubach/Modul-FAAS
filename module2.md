
| Befehl | Funktion |
| ---- | ---- |
| `print("Hello, world!")` | etwas schreiben |
| `\n`| neue output linie in einem print setzten, zb; `print("The itsy bitsy spider\nclimbed up the waterspout.")` |
| `print("The itsy bitsy spider" , "climbed up" , "the waterspout.")` | mit kommas mehrere argumente nacheinander machen |
| `print("My", "name", "is", "Monty", "Python.", sep="-")` | keyword verwenden, hier im beispiel sep="-". Es wird zwischen den zeilen überall "-" ausgegeben, so wird es dann ausgegeben: My-name-is-Monty-Python. |
|`end="*"`| keyword end, wird am ende des satzes verwendet und angegeben |

### Summary

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

| Operator | Funktion |
| -------- | -------- |
| `+` | Addiert zwei Zahlen miteinander. |
| `-` | Subtrahiert die zweite Zahl von der ersten. |
| `*` | Multipliziert zwei Zahlen miteinander. |
| `/` | Teilt die erste Zahl durch die zweite. Das Ergebnis ist immer ein Gleitkommawert (float). |
| `//` | Teilt die erste Zahl durch die zweite und gibt den größten ganzzahligen Wert zurück, der kleiner oder gleich dem Ergebnis ist (ohne Nachkommastellen). |
| `%` | Gibt den Rest der Division der ersten Zahl durch die zweite zurück. |
| `**` | Hebt die erste Zahl auf die Potenz der zweiten Zahl. |

### Summary

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


## Variables

If you want to give a name to a variable, you must follow some strict rules:

the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
the name of the variable must begin with a letter;
the underscore character is a letter;
upper- and lower-case letters are treated as different (a little differently than in the real world – Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
the name of the variable must not be any of Python's reserved words (the keywords – we'll explain more about this soon).

So gibt man eine Variabel an:
```bash
var = 1
print(var)
```

1. A variable is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. (2.1.4.1)

2. Each variable must have a unique name ‒ an identifier. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore(_), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive.

3. Python is a dynamically-typed language, which means you don't need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (=) sign, i.e., var = 1.

4. You can also use compound assignment operators (shortcut operators) to modify values assigned to variables, for example: var += 1, or var /= 5 * 2.

5. You can assign new values to already existing variables using the assignment operator or one of the compound operators

## Comments

Comments can be used to leave additional information in code. They are omitted at runtime. The information left in the source code is addressed to human readers. In Python, a comment is a piece of text that begins with #. The comment extends to the end of the line.

If you want to place a comment that spans several lines, you need to place # in front of them all. Moreover, you can use a comment to mark a piece of code that is not needed at the moment (see the last line of the snippet below), for example:

```bash
# This program prints
# an introduction to the screen.
print("Hello!")  # Invoking the print() function
# print("I'm Python.")
```

### Summary

Whenever possible and justified, you should give self-commenting names to variables, e.g., if you're using two variables to store the length and width of something, the variable names length and width may be a better choice than myvar1 and myvar2.

It's important to use comments to make programs easier to understand, and to use readable and meaningful variable names in code. However, it's equally important not to use variable names that are confusing, or leave comments that contain wrong or incorrect information!

Comments can be important when you are reading your own code after some time (trust us, developers do forget what their own code does), and when others are reading your code (they can help them understand what your programs do and how they do it more quickly).

## Interaction with the user

### Commands

**input ()**

Der user soll etwas antworten, damit das Programm weiterläuft zb:

```bash 
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
``` 

**int()**

the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer; if it fails, the whole program will fail too.

**float()**

the float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float (the rest is the same).

beispiel: 
```bash
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
```

**str()**
 You can also convert a number into a string, which is way easier and safer ‒ this kind of operation is always possible.


### Summary

1. The print() function sends data to the console, while the input() function gets data from the console.

2. The input() function comes with an optional parameter: the prompt string. It allows you to write a message before the user input, e.g.:

```bash
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
```
 
3. When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking (it prompts the user to take action when the console is switched to input mode) until the user has entered an input and/or pressed the Enter key.

*Note*  
You can test the functionality of the input() function in its full scope locally on your machine. For resource optimization reasons, we have limited the maximum program execution time in Edube to a few seconds. Go to the Sandbox, copy-paste the above snippet, run the program, and do nothing ‒ just wait a few seconds to see what happens. Your program should be stopped automatically after a short moment. Now open IDLE, and run the same program there ‒ can you see the difference?

Tip: the above-mentioned feature of the input() function can be used to prompt the user to end a program. Look at the code below:

```bash
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
 
print("\nPress Enter to end the program.")
input()
print("THE END.")
```
 
4. The result of the input() function is a string. You can add strings to each other using the concatenation (+) operator. Check out this code:

```bash
num_1 = input("Enter the first number: ") # Enter 12
num_2 = input("Enter the second number: ") # Enter 21
 
print(num_1 + num_2) # the program returns 1221
```
 
5. You can also multiply (* ‒ replication) strings, e.g.:

```bash
my_input = input("Enter something: ") # Example input: hello
print(my_input * 3) # Expected output: hellohellohello
```