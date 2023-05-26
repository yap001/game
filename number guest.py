import random

def guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != target_number:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

guessing_game()
