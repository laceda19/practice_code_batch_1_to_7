text_input = input("Enter text: ")
if len(text_input) > 0:
    result_text = text_input[0].upper() + text_input[1:].lower()
else:
    result_text = ""
print("Result:", result_text)