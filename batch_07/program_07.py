text_input = input("Enter number: ")
total_length = int(input("Enter length: "))
zeros = total_length - len(text_input)
if zeros > 0:
    result_text = ("0" * zeros) + text_input
else:
    result_text = text_input
print("Result:", result_text)