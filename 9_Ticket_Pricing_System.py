"""
Program: Movie Ticket Pricing System
"""

try:
    user_age = int(input("Enter age: "))
    visit_day = input("Enter day of week: ").strip().lower()
    ticket_count = int(input("Enter number of tickets: "))

    if user_age < 3:
        base_price = 0
    elif 3 <= user_age <= 12:
        base_price = 150
    elif 13 <= user_age <= 59:
        base_price = 300
    else:
        base_price = 200

    discount_rate = 0.20 if visit_day in ["friday", "saturday", "sunday"] else 0

    discounted_price = base_price * (1 - discount_rate)
    total_amount_due = discounted_price * ticket_count

    print("\n--- Ticket Summary ---")
    print("Base Price      :", base_price)
    print("Discount        :", discount_rate * 100, "%")
    print("Final per ticket:", discounted_price)
    print("Total Amount    :", total_amount_due)

except ValueError:
    print("Invalid input provided.")