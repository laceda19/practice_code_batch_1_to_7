text = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")

if text.startswith(prefix):
    text = text[len(prefix):]

print(text)