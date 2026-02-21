try:
    user_input_text = input("Enter word or number: ")
    cleaned_text = user_input_text.lower()

    reversed_text = cleaned_text[::-1]

    print("Original :", user_input_text)
    print("Reversed :", reversed_text)

    if cleaned_text == reversed_text:
        print("Result   : PALINDROME")
    else:
        print("Result   : NOT PALINDROME")

except Exception as err:
    print("Error:", err)