current_num = 0
while current_num <= 100:
    last_digit = current_num % 10
    if last_digit != 0 and last_digit != 5:
        print(current_num)
    current_num = current_num + 1
