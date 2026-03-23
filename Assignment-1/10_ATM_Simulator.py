current_balance_amount = 10000

while True:
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    user_choice = input("Select option: ")

    if user_choice == "1":
        print("Current Balance: ₹", current_balance_amount)

    elif user_choice == "2":
        try:
            deposit_amount = float(input("Enter deposit amount: ₹"))
            if deposit_amount > 0:
                current_balance_amount += deposit_amount
                print("Deposit successful.")
            else:
                print("Deposit must be positive.")
        except ValueError:
            print("Invalid deposit amount.")

    elif user_choice == "3":
        try:
            withdraw_amount = float(input("Enter withdrawal amount: ₹"))
            if withdraw_amount <= 0:
                print("Withdrawal must be positive.")
            elif current_balance_amount - withdraw_amount < 500:
                print("Minimum balance of ₹500 must remain.")
            else:
                current_balance_amount -= withdraw_amount
                print("Withdrawal successful.")
        except ValueError:
            print("Invalid withdrawal amount.")

    elif user_choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid menu choice.")