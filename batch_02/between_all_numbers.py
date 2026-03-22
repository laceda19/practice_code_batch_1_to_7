num1 = float(input("Enter first number:" ))
num2 = float(input("Enter second number:" ))
if num1 < num2:
    start = num1 + 1
    end = num2 - 1
else:
    start = num2 + 1
    end = num1 - 1
print("\nNumbers between", num1, "and", num2, "are:")
current = start
while current <= end:
    print(current)
    current = current + 1
