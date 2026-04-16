text_input = input("Enter text: ")
result_text = ""
for character in text_input:
    if character.isupper():
        result_text = result_text + character.lower()
    else:
        result_text = result_text + character.upper()
print("Result:", result_text)