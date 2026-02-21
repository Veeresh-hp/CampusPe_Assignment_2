def factorial(n):
    if n < 0: return "Invalid"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_digits(n): return sum(int(d) for d in str(abs(n)))
def reverse_number(n): return int(str(n)[::-1])
def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(d)**power for d in str(n))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a*b)//gcd(a,b)
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def math_menu():
    while True:
        print("\n1.Factorial 2.Prime 3.Fibonacci 4.SumDigits 5.Reverse")
        print("6.Armstrong 7.GCD 8.LCM 9.Perfect 10.Exit")

        choice = input("Choose option: ")

        if choice == "10":
            break

        try:
            if choice in ["1","2","3","4","5","6","9"]:
                number = int(input("Enter number: "))

            if choice == "1":
                print("Factorial:", factorial(number))
            elif choice == "2":
                print("Prime:", is_prime(number))
            elif choice == "3":
                print("Fibonacci:", fibonacci(number))
            elif choice == "4":
                print("Sum of digits:", sum_digits(number))
            elif choice == "5":
                print("Reversed:", reverse_number(number))
            elif choice == "6":
                print("Armstrong:", is_armstrong(number))
            elif choice == "7":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a,b))
            elif choice == "8":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a,b))
            elif choice == "9":
                print("Perfect number:", is_perfect(number))
            else:
                print("Invalid option.")

        except ValueError:
            print("Invalid input.")

math_menu()