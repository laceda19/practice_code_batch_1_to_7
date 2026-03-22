valid_numbers = []
while True:
    user_input = (input("Enter a number (or a non-number to stop): "))
    try:
        number = float(user_input)
        valid_numbers.append(number)
        print("Number added!")
    except ValueError:
        print("\nInvalid input. stopping program.")
        break
if len(valid_numbers) > 0:
    valid_numbers.sort()
    print("\nNumber sorted from lowest to highest:")
    for num in valid_numbers:
        print(num)
else:
    print("\nNo valid numbers were entered to sort.")