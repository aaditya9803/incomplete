import random

# Constants for the game
MAX_GUESSES = 5
MAX_NUMBER = 10

# initialize variables
number = random.randint(1, MAX_NUMBER)
num_guesses = 0

# Welcome message
print("Welcome to the AI car game! Guess a number between 1 and {} to win.".format(MAX_NUMBER))

while num_guesses < MAX_GUESSES:
    # get the user's guess
    guess = int(input("Enter your guess: "))

    # increment the number of guesses
    num_guesses += 1

    # check if the guess is correct
    if guess == number:
        print("Congratulations, you won!")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")

# if the user didn't win, print a message
if num_guesses == MAX_GUESSES:
    print("Sorry, you lost. The number was {}.".format(number))
