text = input("Enter a string: ")

is_upper = True

for letter in text:
    if letter >= "a" and letter <= "z":
        is_upper = False
        break

print(is_upper)