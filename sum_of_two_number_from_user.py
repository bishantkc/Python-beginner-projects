def int_number(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(str(num1) + " + " + str(num2) + " = " + str(int_number(num1, num2)))