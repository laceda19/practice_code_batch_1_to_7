text = input("Enter a string: ")

while len(text) > 0 and text[0] == " ":
    text = text[1:]

print(text)