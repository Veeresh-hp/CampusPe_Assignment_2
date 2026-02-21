try:
    first_value = float(input("Enter first number: "))
    second_value = float(input("Enter second number: "))

    print("\n--- Calculation Results ---")
    print(f"Addition        : {first_value + second_value}")
    print(f"Subtraction     : {first_value - second_value}")
    print(f"Multiplication  : {first_value * second_value}")

    if second_value != 0:
        print(f"Division        : {round(first_value / second_value, 2)}")
        print(f"Modulus         : {first_value % second_value}")
    else:
        print("Division & Modulus: Not possible (division by zero)")

    print(f"Exponentiation  : {first_value ** second_value}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")