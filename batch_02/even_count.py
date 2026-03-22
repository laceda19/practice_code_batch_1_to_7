even_count = 0
for i in range(1, 11):
    number = float(input("Enter number {i}: "))
    if number % 2 == 0:
        even_count = even_count + 1
print("Total number is:")
print(even_count)
