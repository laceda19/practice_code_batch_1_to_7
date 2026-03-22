num1 = float(input("Enter dividend:"))
num2 = float(input("Enter divisor:"))
if num2 == 0:
    print("ERROR: cannot be divided by zero!")
else:
    remainder = num1 % num2
    print("Remainder:", remainder)
