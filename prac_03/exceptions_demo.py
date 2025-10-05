"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When an input that cant be converted to an integer is entered
2. When will a ZeroDivisionError occur? WHen the denominator is input as a zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Instead of using except, could just check the input and avoid using except entirely for zerodivisionerror
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# Without using except for ZeroDivisionError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")