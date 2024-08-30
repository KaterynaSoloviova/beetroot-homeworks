# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration.

list_1 = list(range(1, 101))
list_2 = []

i = 0
while i < 100:
    print(list_1[i])
    if list_1[i] % 7 == 0 and list_1[i] % 5 != 0:
        list_2.append(list_1[i])
    i += 1

print(list_2)
