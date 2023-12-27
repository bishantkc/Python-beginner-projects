# Object-Oriented-Programming (OOP)

Object-Oriented Programming (OOP) is a way of writing computer programs that is centered around the concept of "objects". It is a way to organize our code into "classes". 

There are certain concepts or principles in Object-Oriented Programming (OOP) which describes the fundamental ideas and techniques used in OOp to structure and design codes.

1. [Classes](#classes)
2. [Objects](#objects)
3. [Inheritance](#inheritance)
4. [Composition](#composition)
5. [Encapsulation](#encapsulation)
6. [Polymorphism](#polymorphism)

## Classes

* A class is basically a structure that we can use to create an object in our code. 
* It contains set of variables and functions. 
* It defines a data structure and behavior that the objects created from the class will have.

Here's a simple example:
```py
class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.initial_temperature = 25.0

    def say_hi(self):
        print("Hello, my name is " + self.name + ", ready to help!")
```

## Objects

* An object is a fundamental concept that represents a real-world entity or a specific instance of a class. 
* Objects have both data (attributes or properties) and behaviors (methods or functions). 
* An object is created from a class, which serves as a blueprint or template defining the structure and behavior of the object.

Here's a simple example:
```py
class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.initial_temperature = 25.0

    def say_hi(self):
        print("Hello, my name is " + self.name + ", ready to help!")

# Creating an object(instance) of the Robot class    
my_robot = Robot("B5", 4)
my_robot.say_hi()
```

## Inheritance

* Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a new class (subclass or child class) to inherit properties and behaviors from an existing class (superclass or parent class). 
* This concept promotes code reuse by referencing the behaviors and data of an object.
* In other words, a class that inherits from another class shares all the attributes and methods of the referenced class.

Here's a simple example:
```py
# Superclass
class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number

# Subclass
class RoboticArm(Robot):
    def __init__(self, name, version_number, reach):
        # Calling the constructor of superclass
        super().__init__(name, version_number)
        self.reach = reach
    
    
    def pick_object(self, x, y):
        print("Pick object on (" + str(x) + "," + str(y) + ")")

# Creating an object of the subclass
my_robotic_arm = RoboticArm("Bob", 3, 400)
my_robotic_arm.pick_object(4, 5)
```

## Composition

* Composition in Object-Oriented Programming (OOP) is a fundamental concept and describes a class that refers to one or more objects of the other class instance variables.

* Unlike inheritance, which involves creating a new class by extending an existing one, composition focuses on creating relationships between classes by using instances of other classes. 
* Composition promotes code reuse as you can change components without affecting the composite class.
```py
class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self):
        # Composition: Car has an Engine
        self.engine = Engine()

    def drive(self):
        print("Car is moving!")

# Creating an object of the composite class
my_car = Car()

# Invoking methods through composition
my_car.engine.start()
my_car.drive()
```

## Encapsulation

* Encapsulation is a fundamental concept in Object-Oriented Programming (OOP) that involves bundling data (attributes or properties) and the methods (functions or procedures) that operate on the data into a single unit known as an object. 
* The primary goal of encapsulation is to keep the internal details of an object hidden from the outside world and to provide controlled access to the object's functionality.
* Encapsulation is used to hide the values or state of a structured data object inside a class.
```py
class BankAccount:
    def __init__(self, account_holder, balance):
        # Encapsulated attributes
        self._account_holder = account_holder
        self._balance = balance

    # Encapsulated method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    # Encapsulated method
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Encapsulated method
    def get_balance(self):
        return self._balance

# Creating an object of the BankAccount class
my_account = BankAccount(account_holder="John Doe", balance=1000)

# Accessing the object's behavior through encapsulation
my_account.deposit(500)
my_account.withdraw(200)
print(f"Current balance: {my_account.get_balance()}")
```
> In this example, the BankAccount class encapsulates the `attributes (_account_holder and _balance)` and `methods (deposit, withdraw, and get_balance)`. The attributes are marked with a single leading underscore to indicate that they are intended to be protected but can still be accessed.

## Polymorphism

* Polymorphism is a concept in Object-Oriented Programming (OOP) that describes the concept of using different classes with the same interface.
* It allows objects of different classes to be treated as objects of a common base class.
* It promotes clean and readable code by allowing a single method name to represent different behaviors. 

Here's a simple example:
```py
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Creating objects of different classes
generic_animal = Animal()
my_dog = Dog()

# Calling the 'make_sound' method on different objects
generic_animal.make_sound()  # Output: Some generic animal sound
my_dog.make_sound()          # Output: Woof!
```
