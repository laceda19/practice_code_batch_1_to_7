text_input = input("Enter text: ")
total_length = int(input("Enter length: "))
spaces = total_length - len(text_input)
if spaces > 0:
    result_text = (" " * spaces) + text_input
else:
    result_text = text_input
print("Result:", result_text)
