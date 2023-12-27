#for i in range(1):
 #   print("hello " + str(i))

#for i in range(2):
 #   print(i)
  #  i = i + 1

#i=1
#while i <= 5:
 #   print(i)
  #  i += 1

'''
import my_computations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(str(num1) + " + " + str(num2) + " = " + str(my_computations.int_number(num1, num2)))

             or

from my_computations import int_number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(str(num1) + " + " + str(num2) + " = " + str(int_number(num1, num2)))
'''

number_list = [1, 3, -2, 4.5]
for number in number_list:
    print(number)
    if number < 0:
        print("The number is negative.")
    else:
        print("The number is positive.")