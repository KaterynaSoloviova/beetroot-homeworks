# Task 2
# Write a Python program to construct the following pattern,
# using a while loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


star_number = 1
star = "* "
while star_number <= 5:
    print(star * star_number, end="\n")
    star_number += 1
while star_number >= 1:
    print(star * star_number, end="\n")
    star_number -= 1
