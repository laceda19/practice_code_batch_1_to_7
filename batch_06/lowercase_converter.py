text = input("Enter a string: ")

result = ""

for c in text:
    if "A" <= c <= "Z":
        result += chr(ord(c) + 32)
    else:
        result += c

print(result)