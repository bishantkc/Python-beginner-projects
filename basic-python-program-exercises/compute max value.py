def compute_max_value(number_list):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value

number_list = [1, -8, 5, 8, 9]
max_value = compute_max_value(number_list)
print(max_value)