text_input = input("Enter text: ")
while len(text_input) > 0 and text_input[-1] == " ":
    text_input = text_input[:-1]
print("Result:", text_input)