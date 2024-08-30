# Task 4
# The math quiz program
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.

import random

x = random.randint(1, 100)
y = random.randint(1, 100)
math_operation = random.choice(['+', '-', '*', '/'])

print(f"Solve the mathematical equation: {x} {math_operation} {y} = ?")

answer = float(input("Enter your answer: "))

if math_operation == "*":
    correct_answer = x * y
elif math_operation == "+":
    correct_answer = x + y
elif math_operation == "-":
    correct_answer = x - y
elif math_operation == "/":
    correct_answer = x / y

if answer == correct_answer:
    print("It is correct!")
else:
    print(f"No, the correct answer is {correct_answer}")
