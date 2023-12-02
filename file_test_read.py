# import os
# if os.path.exists("new_file"):
#     os.remove("new_file")


# with open("file_test", "r" ) as f:
#     for line in f:
#         print(line.rstrip("\n"))
#
# print("A\nB\nC")

# with open ("new_file", "a") as f:
#     f.write("hello\n ")

# import my_computations
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# print(str(num1) + " + " + str(num2) + " = " + str(my_computations.int_number(num1, num2)))

from my_computations import int_number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(str(num1) + " + " + str(num2) + " = " + str(int_number(num1, num2)))
