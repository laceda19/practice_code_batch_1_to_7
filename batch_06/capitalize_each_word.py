text_input = input("Enter text: ")
words = text_input.split()
result_text = ""
for word in words:
    result_text = result_text + word[0].upper() + word[1:].lower() + " "
print("Result:", result_text.strip())
