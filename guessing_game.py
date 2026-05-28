import random

number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Correct Guess")
        print("Attempts:", attempts)
        break

    elif guess > number:
        print("Too High")

    else:
        print("Too Low")