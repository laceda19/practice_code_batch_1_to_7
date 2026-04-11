name = input("Enter your full name: ")
print(''.join(word.capitalize() for word in name.split()))