first_num = float(input("Enter a NUMBER (this is the starting number):" ))
result = first_num
for i in range(9):
    current_num_order = i +2
    remaining_num = float(input(f"Enter NUMBER {current_num_order}: "))
    result = result - remaining_num
print("FINAL RESULT: First number minus all remaining 9 number =", result)

