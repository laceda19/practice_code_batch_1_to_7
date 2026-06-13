text_input = input("Enter text: ")
prefix = input("Enter starting text to check: ")
if text_input[:len(prefix)] == prefix:
    print("True")
else:
    print("False")
