numbers_list = []
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        numbers_list.append(int(user_input))
    else:
        print("Invalid input. Stop.")
        break
if len(numbers_list) > 0:
    numbers_list.sort(reverse=True)
    print("Numbers from highest to lowest:")
    for current_number in numbers_list:
        print(current_number)
else:
    print("No valid numbers entered.")