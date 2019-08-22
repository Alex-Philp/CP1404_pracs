"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when input value is not of the correct data type during a mathematical operation
making said operation impossible
2. When will a ZeroDivisionError occur?
when attempting to divide by zero, as it is an indefinite number
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("cannot divide by 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
# print("Cannot divide by zero!")
print("Finished.")
