# quotient of input numbers (with decimal point)
#input dividend
dividend = float(input("Enter dividend: "))
#input divisor
divisor = float(input("Enter divisor: "))
if divisor == 0:
    print("error")
else:
    quotient = dividend / divisor
    print("The quotient of two numbers is:", quotient)
