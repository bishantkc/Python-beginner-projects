def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1/2/3/4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:  #if int is not used in choice " " should be applied
    print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))

elif choice == 2:
    print(str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))

elif choice == 3:
    print(str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2)))

elif choice == 4:
    print(str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))
else:
    print("Invalid input")