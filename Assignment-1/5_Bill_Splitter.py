try:
    total_bill_amount = float(input("Enter total bill amount: ₹"))
    total_people_count = int(input("Enter number of people: "))
    tax_percent = float(input("Enter tax percentage: "))
    tip_percent = float(input("Enter tip percentage: "))

    tax_value = total_bill_amount * (tax_percent / 100)
    after_tax_total = total_bill_amount + tax_value
    tip_value = after_tax_total * (tip_percent / 100)
    final_bill_total = after_tax_total + tip_value

    if total_people_count > 0:
        amount_each = final_bill_total / total_people_count
    else:
        amount_each = 0

    print("\n==== BILL SUMMARY ====")
    print(f"Subtotal     : ₹{total_bill_amount:.2f}")
    print(f"Tax Amount   : ₹{tax_value:.2f}")
    print(f"After Tax    : ₹{after_tax_total:.2f}")
    print(f"Tip Amount   : ₹{tip_value:.2f}")
    print(f"Final Total  : ₹{final_bill_total:.2f}")
    print(f"Per Person   : ₹{amount_each:.2f}")

except ValueError:
    print("Invalid input detected. Please enter correct numeric values.")