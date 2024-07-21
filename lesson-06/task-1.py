# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

list = []

while len(list) < 10:
    list.append(random.randint(0, 100))

i = 0
max = list[0]
while i < 9:
    if max < list[i + 1]:
        max = list[i + 1]
    i += 1

print(list)
print(f"The max number in the list is {max}")


