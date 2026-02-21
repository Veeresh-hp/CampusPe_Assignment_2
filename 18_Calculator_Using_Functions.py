"""
Program: Functional Calculator
"""

def addition(a, b): return a + b
def subtraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b): return a / b if b != 0 else "Division by zero error"
def modulus(a, b): return a % b
def power(a, b): return a ** b

def calculator_menu():
    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Pow 7.Exit")
        option = input("Choose option: ")

        if option == "7":
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operations = {
                "1": addition,
                "2": subtraction,
                "3": multiplication,
                "4": division,
                "5": modulus,
                "6": power
            }

            if option in operations:
                print("Result:", operations[option](num1, num2))
            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid numeric input.")

calculator_menu()