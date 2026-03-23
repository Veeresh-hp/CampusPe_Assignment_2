import random

best_attempt_score = None

while True:
    secret_value = random.randint(1, 100)
    attempts_remaining = 7
    attempts_used = 0

    print("\nGuess the number between 1 and 100")

    while attempts_remaining > 0:
        try:
            user_guess = int(input("Enter guess: "))
            attempts_used += 1
            attempts_remaining -= 1

            if user_guess == secret_value:
                print(f"Correct! You guessed in {attempts_used} attempts.")
                if best_attempt_score is None or attempts_used < best_attempt_score:
                    best_attempt_score = attempts_used
                break
            elif user_guess > secret_value:
                print("Too High!")
            else:
                print("Too Low!")

            if abs(user_guess - secret_value) <= 5:
                print("Hint: Very close!")

            print("Attempts left:", attempts_remaining)

        except ValueError:
            print("Enter valid integer.")

    else:
        print("Game Over! Number was:", secret_value)

    print("Best score so far:", best_attempt_score)

    replay = input("Play again? (yes/no): ").lower()
    if replay != "yes":
        break