numbers_list = []
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        numbers_list.append(int(user_input))
    else:
        break
most_duplicate_number = numbers_list[0]
highest_count = 0
for current_number in numbers_list:
    if numbers_list.count(current_number) > highest_count:
        highest_count = numbers_list.count(current_number)
        most_duplicate_number = current_number
print("Most duplicate:", most_duplicate_number)
print("Count:", highest_count)