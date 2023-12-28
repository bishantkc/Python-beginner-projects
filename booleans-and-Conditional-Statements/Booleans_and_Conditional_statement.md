# Booleans in Programming

* Booleans are a fundamental data type in programming used to represent truth values. 
* In most programming languages, a boolean can have one of two values: `True` or `False`. 
* Booleans are essential for decision-making and controlling the flow of a program through conditional statements.

### **Table of Contents**

1. [Boolean Operators](#boolean-operators)
    * A. [And Operator(`and`)](#a-and-operator-and)
    * B. [OR Operator(`or`)](#b-or-operator-or)
    * C. [NOT Operator(`not`)](#c-not-operator-not)
1. [Comparison Operators](#comparison-operators)
    * A. [Equality or Equal To(`==`)](#a-equality-or-equal-to)
    * B. [Inequality or Not Equal To(`!=`)](#b-inequality-or-not-equal-to)
    * C. [Greater Than (`>`) or Greater Than or Equal To (`>=`)](#c-greater-than--or-greater-than-or-equal-to)
    * D. [Less Than (`<`) or Less Than or Equal To (`<=`)](#d-less-than--or-less-than-or-equal-to)
1. [Conditional Statements](#conditional-statements)
    1. [If Statement](#1-if-statement)
    2. [If-Else Statement](#2-if-else-statement)
    3. [If-Elif-Else Statement](#3-if-elif-else-statement)
    4. [Ternary Operator](#4-ternary-operator)

## Boolean Operators

* Boolean operators are logical operators that operate on Boolean values, producing a Boolean result.
* They are often used to combine or modify the logic of conditions.

### A. And Operator (`and`):

* The `and` operator returns `True` only if both operands are `True`; otherwise, it returns `False`.

Here's a simple example:
```py
x = True
y = False
result = x and y  # Result is False
```

### B. OR Operator (`or`):

* The `or` operator returns `True` if at least one of the operands is `True`; if both are `False`, it returns `False`.

Here's a simple example:
```py
x = True
y = False
result = x or y  # Result is True
```

### C. NOT Operator (`not`):

* The `not` operator returns the opposite Boolean value of its operand. 
* If the operand is `True`, `not` returns `False`; if the operand is `False`, `not` returns `True`.

Here's a simple example:
```py
x = True
result = not x  # Result is False
```

## Comparison Operators

* Comparison operators are used to compare two values and evaluate to a Boolean result (either `True` or `False`).

### A. Equality or Equal To (`==`):

* Checks if the values on the left and right are equal.
```py
x = 5
y = 5
result = x == y  # Result is True
```

### B. Inequality or Not Equal To (`!=`):

* Checks if the values on the left and right are not equal.
```py
x = 5
y = 10
result = x != y  # Result is True
```

### C. Greater Than (`>`) or Greater Than or Equal To (`>=`):

* **`Greater than(>)`** checks if the value on the left is greater than the value on the right.
* **`Greater Than or Equal To (>=)`** Checks if the value on the left is greater than or equal to the value on the right.
```py
# Greater than
x = 10
y = 5
result = x > y  # Result is True

# Greater than or Equal to
x = 10
y = 10
result = x >= y  # Result is True
```

### D. Less Than (`<`) or Less Than or Equal To (`<=`):

* **`Less Than (<)`** checks if the value on the left is less than the value on the right.
* **`Less Than or Equal To (<=)`** checks if the value on the left is less than or equal to the value on the right.
```py
# Less than
x = 5
y = 10
result = x < y  # Result is True

# Less than or Equal to
x = 5
y = 5
result = x <= y  # Result is True
```

## Conditional Statements

* Conditional statements allow programs to make decisions and execute different blocks of code based on whether a specified condition evaluates to `True` or `False`.
* Booleans are often used in conditional statements to control the flow of a program. 
* Conditional statements are implemented using `if`, `else`, and `elif` (else if) constructs.

### 1. If Statement

* The `if` statement is used to execute a block of code if a specified condition is `True`.
```py
# Example: Check if a number is positive
num = 10
if num > 0:
    print("The number is positive.")
```

### 2. If-Else Statement

* The `if-else` statement is used to execute one block of code if the condition is `True` and another block if the condition is `False`.
```py
# Example: Check if a number is positive or negative
num = -5
if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")
```

### 3. If-Elif-Else Statement

* The `if-elif-else` statement is used when there are multiple conditions to check.
```py
# Example: Categorize a number as positive, negative, or zero
num = 0
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### 4. Ternary Operator

* Ternary Operator is a concise way to write simple `if-else` statements in a single line.
```py
# Example: Ternary operator to determine if a number is even or odd
num = 7
result = "even" if num % 2 == 0 else "odd"
print(f"The number is {result}.")
```