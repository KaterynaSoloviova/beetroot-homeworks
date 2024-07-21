# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# "Hello <name>, on your next birthday you’ll be <age+1> years"

input_name = input("Please enter your name: ")
input_age = int(input("Please enter your age: "))

print(f"Hello {input_name}, on your next birthday you’ll be {input_age + 1} years")