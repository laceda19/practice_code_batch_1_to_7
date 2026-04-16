numbers_list = []
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        numbers_list.append(int(user_input))
    else:
        print("Invalid input. Stop.")
        break
if len(numbers_list) > 0:
    highest_number = numbers_list[0]
    for current_number in numbers_list:
        if current_number > highest_number:
            highest_number = current_number
    print("Highest number:", highest_number)
else:
    print("No valid numbers entered.")