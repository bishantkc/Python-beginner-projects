def compute_list_average(number_list):
    return sum(number_list) / len(number_list)

number_list = []
ask_number_from_user = True
while ask_number_from_user:
    user_input = float(input("Enter a number: "))
    if user_input == 0.0:
        ask_number_from_user = False
    else:
        number_list.append(user_input)
print(compute_list_average(number_list))