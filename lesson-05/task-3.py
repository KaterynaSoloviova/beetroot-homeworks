# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of
# the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string

import random

input_string = input('Enter a string: ')
original_string = input_string


for i in range(5):
    new_string = ""
    input_string = original_string
    while len(input_string) > 0:
        index = random.randint(0, len(input_string) - 1)
        new_string = new_string + input_string[index]
        input_string = input_string[0:index] + input_string[index + 1:]

    print(f"{new_string}")
