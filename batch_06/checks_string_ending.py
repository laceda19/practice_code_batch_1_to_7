text = input("Enter a string: ")
ending = input("Enter ending: ")

print(text[-len(ending):] == ending)
