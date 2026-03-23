all_numbers = []
for i in range(10):
    num = float(input("Enter a number {i+1}: "))
    all_numbers.append(num)
duplicate_numbers = []
checked_numbers = []
for num in all_numbers:
    if num not in checked_numbers:
        count = all_numbers.count(num)
        if count > 1:
         duplicate_numbers.append(num)
         checked_numbers.append(num)
print("----RESULT----")
if duplicate_numbers:
    print("Numbers with duplicates:")
    for dup in duplicate_numbers:
        print(dup)
else:
    print("No numbers have duplicates!")



