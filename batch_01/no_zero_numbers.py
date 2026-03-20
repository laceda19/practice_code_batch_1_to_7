# numbers from o to 100 except those ending in zero
for number in range(0, 101):
    if number % 10 == 0:
        #skip if ends with zero
        continue
    print(number)