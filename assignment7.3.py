try:
    dividend = int(input("Please enter the dividend: "))
except ValueError:
    print("The dividend has to be a number!")

try:
    divisor = int(input("Please enter the divisor: "))
except ValueError:
    print("The divisor has to be a number!")

try:
    print("dividend / divisor = f" / (dividend, divisor, dividend/divisor))
except ZeroDivisionError:
    print("divison by zero!")

		
