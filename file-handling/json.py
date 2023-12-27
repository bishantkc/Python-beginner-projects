import simplejson as json
import os

if os.path.isfile("data/ages_json"): #its similar to checking .exist in place of isfile
    old_file = open("data/ages_json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = int(data["age"]) + 1
    print("New age is", data["age"])
else:
    old_file = open("data/ages_json", "w+")
    data = {"name": "John", "age": "18"}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
