"""
Program: Personal Bio Card
Description: Displays student information in a formatted card.
"""

# Assigning personal details to variables
student_full_name = "Veeresh"
student_age_year = 21
enrolled_course = "Python Programming"
college_name = "XYZ Institute of Technology"
contact_email = "veeresh@gmail.com"

# Creating formatted card
print("\n" + "=" * 40)
print(" " * 12 + "STUDENT PROFILE")
print("=" * 40)
print(f"Name    : {student_full_name}")
print(f"Age     : {student_age_year} year")
print(f"Course  : {enrolled_course}")
print(f"College : {college_name}")
print(f"Email   : {contact_email}")
print("=" * 40)