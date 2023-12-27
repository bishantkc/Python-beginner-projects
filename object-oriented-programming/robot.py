class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.initial_temperature = 25.0

    def say_hi(self):
        print("Hello, my name is " + self.name + ", ready to help!")

    def init_hardware(self):
        print("Init hardware")

    def print_info(self):
        self.say_hi()
        print("Version number: " + str(self.version_number))
        print("Temperature: " + str(self.initial_temperature))

class RoboticArm(Robot):
    def __init__(self, name, version_number, reach):
        super().__init__(name, version_number)
        self.reach = reach

    def pick_object(self, x, y):
        print("Pick object on (" + str(x) + "," + str(y) + ")")

    def place_object(self, x, y):
        print("Place object on (" + str(x) + "," + str(y) + ")")

class PackagingSolution:
    def __init__(self, robot_right, robot_left):
        self.robot_right = robot_right
        self.robot_left = robot_left

    def package(self, pick_x, pick_y, middle_x, middle_y, place_x, place_y):
        self.robot_right.pick_object(pick_x, pick_y)
        self.robot_right.place_object(middle_x, middle_y)
        self.robot_left.pick_object(middle_x, middle_y)
        self.robot_left.place_object(place_x, place_y)
