"""
Program: Advanced Text Analyzer
"""

def count_words(text): return len(text.split())
def count_vowels(text): return sum(1 for ch in text.lower() if ch in "aeiou")
def count_consonants(text): return sum(1 for ch in text.lower() if ch.isalpha() and ch not in "aeiou")
def reverse_text(text): return text[::-1]
def is_palindrome(text): return text.lower() == text[::-1].lower()
def remove_vowels(text): return "".join(ch for ch in text if ch.lower() not in "aeiou")
def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq
def longest_word(text): return max(text.split(), key=len)

def analyze_text():
    user_text = input("Enter text: ")

    print("\n--- TEXT ANALYSIS ---")
    print("Words:", count_words(user_text))
    print("Vowels:", count_vowels(user_text))
    print("Consonants:", count_consonants(user_text))
    print("Reversed:", reverse_text(user_text))
    print("Palindrome:", is_palindrome(user_text))
    print("Without vowels:", remove_vowels(user_text))
    print("Longest word:", longest_word(user_text))
    print("Word frequency:", word_frequency(user_text))

analyze_text()