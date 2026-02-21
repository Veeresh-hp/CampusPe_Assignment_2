try:
    base_number = int(input("Enter base number: "))
    end_range = int(input("Enter range end value: "))

    print(f"\nMultiplication Table of {base_number}\n")

    for multiplier in range(1, end_range + 1):
        print(f"{base_number} x {multiplier} = {base_number * multiplier}")

except ValueError:
    print("Please enter valid integers.")