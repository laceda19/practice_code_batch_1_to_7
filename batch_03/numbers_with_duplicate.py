all_inputs = []
shown_numbers = []
for i in range (1, 11):
    num = float(input("Enter number {i}:" ))
    all_inputs.append(num)
print("Numbers that has duplicates:")
for num in all_inputs:
    if num not in shown_numbers:
        print(num)
        shown_numbers.append(num)
