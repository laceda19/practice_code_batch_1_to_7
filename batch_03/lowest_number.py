all_numbers = []
for i in range(1, 11):
    num = float(input("Enter number {i}: "))
    all_numbers.append(num)
lowest_num = min(all_numbers)
print ("The lowest number you entered is:")
print(lowest_num)
