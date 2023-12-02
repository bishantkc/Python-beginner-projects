city_list = []

with open("data/cities", "r") as f:
    for line in f:
        city_list.append(line.rstrip("\n"))

sorted_city_list = sorted(city_list)

with open("data/ordered_cities", "w") as f:
    for city in sorted_city_list:
        f.write(city + "\n")

while True:
    pass

print("Done")
