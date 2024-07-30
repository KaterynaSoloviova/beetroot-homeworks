# Task 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random

number_generated = random.randint(1, 10)
number_input = int(input("Enter an integer number between 1 and 10: "))
attempts = 1
while number_input != number_generated:
    print("Oopps, try again!")
    number_input = int(input("Enter an integer number between 1 and 10: "))
    attempts += 1

if attempts == 1:
    print("Unbelievable! You guessed right on the first attempt!")
elif attempts <= 3:
    print(f"Well done! You guessed right on the {attempts} attempt!")
else:
    print(f"Finally you guessed the number! You had {attempts} attempts.")


