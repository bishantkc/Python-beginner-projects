from robot import Robot
from robot import RoboticArm
from robot import PackagingSolution

my_robot = Robot("B5", 4)
my_robot.say_hi()
my_robot.init_hardware()
my_robot.print_info()

print(my_robot.name)
my_robot2 = Robot("V4", 2)
my_robot2.print_info()

my_robotic_arm = RoboticArm("Bob", 3, 400)
my_robotic_arm.print_info()
my_robotic_arm.pick_object(4, 5)
my_robotic_arm.place_object(8, 9)

robotic_arm_right = RoboticArm("John", 4, 300)
robotic_arm_left = RoboticArm("Don", 5, 200)
packaging_solution = PackagingSolution(robotic_arm_right, robotic_arm_left)
packaging_solution.package(1,2,3,4,5,6)
