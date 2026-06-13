text_input = input("Enter text: ")
has_letter = False
all_lower = True
for character in text_input:
    if character.isalpha():
        has_letter = True
        if not ("a" <= character <= "z"):
            all_lower = False
if has_letter and all_lower:
    print("True")
else:
    print("False")
