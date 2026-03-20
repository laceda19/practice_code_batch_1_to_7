# This program ask for 2 numbers and print the bigger one
# Input 1
num1 = float(input("Enter the first number: "))
# Input 2
num2 = float(input("Enter the second number: "))
# Check which number is bigger
if num1 > num2:
    # If first number is bigger
    print("The bigger number is:", num1)
elif num2 > num1:
    # If second number is bigger
    print("The bigger number is:", num2)
else:
    # If both numbers are equal
    print("both numbers are equal")