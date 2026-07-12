# Number Guessing Game

secret_number = 7
tries = 3

for i in range(tries):
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess!")

        if i < tries - 1:
            print("Try again.")
            continue
        else:
            print("Game Over! The correct number was", secret_number)
