"""
Program: Temperature Conversion Tool
"""

def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return (f - 32) * 5/9 + 273.15
def k_to_f(k): return (k - 273.15) * 9/5 + 32

while True:
    print("\n1.C→F 2.F→C 3.C→K 4.K→C 5.F→K 6.K→F 7.Exit")
    choice_option = input("Choose option: ")

    if choice_option == "7":
        print("Exiting program.")
        break

    try:
        temperature_input = float(input("Enter temperature value: "))

        if choice_option == "1":
            print("Converted:", c_to_f(temperature_input))
        elif choice_option == "2":
            print("Converted:", f_to_c(temperature_input))
        elif choice_option == "3":
            print("Converted:", c_to_k(temperature_input))
        elif choice_option == "4":
            print("Converted:", k_to_c(temperature_input))
        elif choice_option == "5":
            print("Converted:", f_to_k(temperature_input))
        elif choice_option == "6":
            print("Converted:", k_to_f(temperature_input))
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numeric temperature.")