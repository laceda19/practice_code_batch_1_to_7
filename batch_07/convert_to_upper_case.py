text_input = input("Enter text: ")
result_text = ""
for character in text_input:
    if "a" <= character <= "z":
        result_text = result_text + chr(ord(character) - 32)
    else:
        result_text = result_text + character
print("Result:", result_text)
