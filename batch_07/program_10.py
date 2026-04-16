text_input = input("Enter text: ")
search_char = input("Enter character: ")
position = -1
for i in range(len(text_input)):
    if text_input[i] == search_char:
        position = i
print("Last Index:", position)