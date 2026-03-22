all_numbers = []
for i in range (1, 11):
    num = float(input("Enter number {i}: "))
    all_numbers.append(num)
unique_numbers = []
for num in all_numbers:
    count = all_numbers.count(num)
    if count == 1 and num not in unique_numbers:
        unique_numbers.append(num)
print("\nNumbers that dont have duplicates:")
if len(unique_numbers) > 0:
    for num in unique_numbers:
        print(num)
else:
    print("No duplicate numbers found!")
