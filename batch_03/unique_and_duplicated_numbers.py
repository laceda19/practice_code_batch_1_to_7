saved_numbers = []
while True:
    user_input = (input("\nEnter a number (or non-number to stop): "))
    try:
        number = float(user_input)
        if number in saved_numbers:
            print("DUPLICATE")
        else:
            print("UNIQUE")
            saved_numbers.append(number)
    except ValueError:
        print("\nInvalid input - stopping program.")
        break


