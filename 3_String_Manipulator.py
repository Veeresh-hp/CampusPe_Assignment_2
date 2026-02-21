"""
Program: Sentence Analyzer
Description: Performs various string operations.
"""

try:
    user_sentence = input("Enter a sentence: ").strip()

    words_list = user_sentence.split()

    print("\n--- Sentence Analysis ---")
    print("Original               :", user_sentence)
    print("Characters (with space):", len(user_sentence))
    print("Characters (no space)  :", len(user_sentence.replace(" ", "")))
    print("Total Words            :", len(words_list))
    print("UPPERCASE              :", user_sentence.upper())
    print("lowercase              :", user_sentence.lower())
    print("Title Case             :", user_sentence.title())

    if words_list:
        print("First Word             :", words_list[0])
        print("Last Word              :", words_list[-1])
    else:
        print("No words entered.")

    print("Reversed Sentence      :", user_sentence[::-1])

except Exception as error:
    print("Unexpected error occurred:", error)