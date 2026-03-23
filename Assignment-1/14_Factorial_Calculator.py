try:
    number_input = int(input("Enter a number: "))

    if number_input < 0:
        print("Factorial is not defined for negative numbers.")
    elif number_input == 0:
        print("0! = 1")
    else:
        result_value = 1
        calculation_steps = []

        for num in range(number_input, 0, -1):
            result_value *= num
            calculation_steps.append(str(num))

        print(f"{number_input}! = {' x '.join(calculation_steps)} = {result_value}")

except ValueError:
    print("Please enter a valid integer.")