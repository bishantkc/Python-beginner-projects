# Loops in Programming

* Loops are fundamental constructs in programming that allow a set of instructions to be repeated multiple times. 
* A Loop is used to execute a group of instructions or a block of code multiple times, without writing it repeatedly. 
* They help automate repetitive tasks and iterate over collections of data. 
* There are two main types of loops: 
    * **for loops**  
    * **while loops**

### **Table of Contents**

1. [For Loops](#for-loops)
    + A. [Nested `for` Loops](#a-nested-for-loops)
1. [While Loops](#while-loops)
1. [Loop Control Statements](#loop-control-statements)
    + A. [Break](#a-break)
    + B. [Continue](#b-continue)
    + C. [Pass](#c-pass)
1. [Infinite Loops](#infinite-loops)

## For Loops

* A **`for`** loop is used when the number of iterations is known in advance. 
* It typically iterates over a sequence of elements, such as a range of numbers or items in a list.

Here's a simple example:
```py
for num in range(1, 6):
    print(num) # Print numbers from 1 to 5

# Another example
def compute_max_value(number_list):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value

number_list = [1, -8, 5, 8, 9]
max_value = compute_max_value(number_list)
print(max_value) # Prints 9
```

### A. Nested `for` Loops

* A nested **`for`** loop is a loop structure within another loop.
* It involves placing one for loop inside another, allowing for the execution of the inner loop for each iteration of the outer loop.
* This creates a two-dimensional iteration, where the inner loop runs multiple times for each iteration of the outer loop.

Here's a simple example:
```py
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t") 
        # /t adds tab at the end of each iteration
    print() #This prints a new line like(\n)
```

## While Loops

* A while loop is used when the number of iterations is not known in advance, and the loop continues as long as a specified condition is true.
* The loop consists of a set of instructions, and the condition is evaluated before each iteration. 
* If the condition is true, the block of code is executed; otherwise, the loop terminates, and the program continues with the next set of instructions after the loop.

Here's a simple example:
```py
num = 1
while num <= 5:
    print(num)
    num += 1
    # Print numbers from 1 to 5 using a while loop
```

## Loop Control Statements

### A. Break:

* It terminates the loop prematurely based on a certain condition.
* When a break statement is encountered within a loop, the loop is terminated, and the program continues with the next statement after the loop.

Here's a simple example:
```py
# for loop
for i in range(1, 6):
    if i == 3:
        break  # Exits the loop when i is 3
    print(i)

# while loop
count = 1
while count <= 5:
    if count == 3:
        break  # Exits the loop when count is 3
    print(count)
    count += 1
```

### B. Continue:

* It skips the rest of the code in the current iteration and moves to the next iteration.
* When a continue statement is encountered, the current iteration of the loop is terminated immediately, and the program proceeds to the next iteration (if any).
* In other words, the remaining code in the loop for the current iteration is skipped, and the loop moves on to the next iteration.

Here's a simple example:
```py
# for loop
for i in range(1, 6):
    if i == 3:
        continue  # Skips the rest of the loop for i == 3
    print(i)

# while Loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skips the rest of the loop for count == 3
    print(count)
```

### C. Pass

* The `pass` statement is a null operation.
* It serves as a placeholder where syntactically some code is required but no action needs to be taken or specified.

Heres a simple example:
```py
# for loop
for i in range(5):
    if i == 2:
        pass  # Does nothing when i is 2
    else:
        print(i)

# while loop
count = 0
while count < 5:
    if count == 2:
        pass  # Does nothing when count is 2
    else:
        print(count)
    count += 1
```

* The pass statement is also commonly used in situations where you are outlining the structure of your code but haven't implemented the details yet.

Example:
```py
def my_function():
    # To be implemented later
    pass
```


## Infinite Loops

* An infinite loop is a loop that continues to execute indefinitely because the loop condition always evaluates to true.
* It's important to avoid unintentional infinite loops, as they can cause a program to hang or become unresponsive.
* It continues indefinitely until the program is interrupted or a break condition is met.

Here's a simple example:
```py
count = 0
while count < 5:
    print("This loop will never end!")

          #or

while True:
    print("This is an infinite loop!")