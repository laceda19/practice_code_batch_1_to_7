numbers_list = []
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        numbers_list.append(int(user_input))
    else:
        print("Invalid input. Stop.")
        break
if len(numbers_list) > 0:
    total_sum = sum(numbers_list)
    count_numbers = len(numbers_list)
    average_value = total_sum / count_numbers
    print("Average:", average_value)
else:
    print("No valid numbers entered.")