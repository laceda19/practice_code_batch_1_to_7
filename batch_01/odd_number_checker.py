# print how many of 10 input numbers are odd
odd_count = 0
for i in range(10):
    number = float(input(f"Enter a number {i+1}: "))
    if number % 2 == 1 or number % 2 == -1:
        odd_count = odd_count + 1
print("The number  of odd numbers is:", odd_count)  
