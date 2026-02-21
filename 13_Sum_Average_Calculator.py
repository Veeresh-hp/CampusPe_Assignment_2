try:
    count_numbers = int(input("How many numbers will you enter? "))
    if count_numbers <= 0:
        raise ValueError("Count must be greater than zero.")

    collected_numbers = []

    for index in range(count_numbers):
        value = float(input(f"Enter number {index + 1}: "))
        collected_numbers.append(value)

    total_sum = sum(collected_numbers)
    average_value = total_sum / count_numbers
    maximum_value = max(collected_numbers)
    minimum_value = min(collected_numbers)

    print("\n--- Results ---")
    print("Sum     :", total_sum)
    print("Average :", average_value)
    print("Maximum :", maximum_value)
    print("Minimum :", minimum_value)

except ValueError as e:
    print("Input Error:", e)