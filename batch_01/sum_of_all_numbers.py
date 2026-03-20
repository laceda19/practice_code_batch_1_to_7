#print the sum of 10 numbers
total_sum = 0
for i in range (10):
    number = float(input(f"Enter a number {i+1}: "))
    total_sum = total_sum + number
print("The sum of all 10 numbers is:", total_sum)
