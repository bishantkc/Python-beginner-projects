
def odd_even(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 in range(2,5):
        print("Not Weird")
    elif n % 2 == 0 in range(6,20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

number = int(input("Enter a number: "))
result = odd_even(number)

