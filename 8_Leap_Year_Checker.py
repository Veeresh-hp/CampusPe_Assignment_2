"""
Program: Leap Year Validator
"""

try:
    year_input_value = int(input("Enter year to check: "))

    if (year_input_value % 4 == 0 and year_input_value % 100 != 0) or (year_input_value % 400 == 0):
        print(f"{year_input_value} is a Leap Year.")
    else:
        print(f"{year_input_value} is NOT a Leap Year.")

except ValueError:
    print("Invalid year entered.")