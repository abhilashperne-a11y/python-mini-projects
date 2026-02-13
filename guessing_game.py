import random

secret = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

while True:
    guess = input("Enter your guess (or type 'q' to quit): ")

    if guess.lower() == 'q':
        print("You quit the game. The number was:", secret)
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low ⬇️")
    elif guess > secret:
        print("Too high ⬆️")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break