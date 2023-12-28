num = int(input("Enter a number: "))
count = 0

if num > 1:
    for i in range(1,num+1): # num+1 will make range equal to the number input
        if (num % i) == 0:
            count = count + 1

    if count == 2:
            print("It is prime number.")
    else:
            print("It is not a prime number.")