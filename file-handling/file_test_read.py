
import os
if os.path.exists("new_file"):
    os.remove("new_file")

     # or

file_name = "new_file"
if os.path.exists(file_name):
    os.remove(file_name)



with open("file_test", "r" ) as f:
    for line in f:
        print(line.rstrip("\n"))

print("A\nB\nC")

with open ("new_file", "a") as f:
    f.write("hello\n ")

