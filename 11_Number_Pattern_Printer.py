def pattern_one(rows):
    for line in range(1, rows + 1):
        print(" ".join(str(num) for num in range(1, line + 1)))

def pattern_two(rows):
    for line in range(1, rows + 1):
        print(" ".join([str(line)] * line))

def pattern_three(rows):
    for line in range(rows, 0, -1):
        print(" ".join(str(num) for num in range(line, 0, -1)))

def pattern_four(rows):
    for line in range(1, rows + 1):
        ascending = list(range(1, line + 1))
        descending = list(range(line - 1, 0, -1))
        full_line = ascending + descending
        print("".join(map(str, full_line)))

try:
    print("\nSelect Pattern (1-4)")
    user_option = int(input("Enter pattern number: "))
    height_value = int(input("Enter height: "))

    if height_value <= 0:
        raise ValueError("Height must be positive.")

    print("\n--- Generated Pattern ---")

    if user_option == 1:
        pattern_one(height_value)
    elif user_option == 2:
        pattern_two(height_value)
    elif user_option == 3:
        pattern_three(height_value)
    elif user_option == 4:
        pattern_four(height_value)
    else:
        print("Invalid pattern selection.")

except ValueError as ve:
    print("Input Error:", ve)