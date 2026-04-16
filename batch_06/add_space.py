text_input = input("Enter text: ")
total_length = int(input("Enter length: "))
result_text = text_input
while len(result_text) < total_length:
    result_text = result_text + " "
print("Result:", result_text)


