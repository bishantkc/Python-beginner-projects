def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

Celsius_degree = int(input("Enter celsius degree: "))
print(str(Celsius_degree) + " C " + " = " + str(celsius_to_fahrenheit(Celsius_degree)) + " F " )
