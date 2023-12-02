def hello(user_name, user_age):
    print("Hello " + user_name + ", you are " +str(user_age))
#hello("Bishant", "18")

def user(number):
    return number * 2

def double_user(number):
    result =  user(number)
    print("Double of " + str(number) + " is " + str(result))
double_user(4)
