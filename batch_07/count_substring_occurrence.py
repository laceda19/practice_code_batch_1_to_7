text_input = input("Enter text: ")
search_char = input("Enter character to count: ")
counter = 0
for character in text_input:
    if character == search_char:
        counter = counter + 1
print("Count:", counter)
