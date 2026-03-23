from datetime import datetime

try:
    birth_year_input = int(input("Enter your birth year: "))
    current_year = datetime.now().year

    if birth_year_input > current_year:
        print("Birth year cannot be in the future.")
    else:
        age_years = current_year - birth_year_input
        age_months = age_years * 12
        age_days = age_years * 365
        age_hours = age_days * 24
        age_minutes = age_hours * 60

        print("\n--- Age Details ---")
        print("Age in Years   :", age_years)
        print("Age in Months  :", age_months)
        print("Age in Days    :", age_days)
        print("Age in Hours   :", age_hours)
        print("Age in Minutes :", age_minutes)
        print("Years until 100:", 100 - age_years)

except ValueError:
    print("Please enter a valid numeric year.")