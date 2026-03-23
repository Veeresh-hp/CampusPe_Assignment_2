def check_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if num % divisor == 0:
            return False
    return True

try:
    single_number = int(input("Enter a number to check prime: "))

    if check_prime(single_number):
        print(f"{single_number} is PRIME")
    else:
        print(f"{single_number} is NOT PRIME")

    start_range = int(input("Enter start range: "))
    end_range = int(input("Enter end range: "))

    primes_list = [n for n in range(start_range, end_range + 1) if check_prime(n)]

    print("Prime numbers in range:", primes_list)

except ValueError:
    print("Invalid input.")