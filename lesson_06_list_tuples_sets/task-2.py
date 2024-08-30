# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

list_1 = []
list_2 = []
list_3 = []
list_4 = []

while len(list_1) < 10:
    list_1.append(random.randint(1, 10))

while len(list_2) < 10:
    list_2.append(random.randint(1, 10))

print(list_1)
print(list_2)

i = 0
while i < 10:
    if list_1[i] in list_2:
        if list_1[i] in list_3:
            list_3.remove(list_1[i])
        list_3.append(list_1[i])
    i += 1

print(list_3)

# The second version:
i = 0
while i < 10:
    if list_1[i] in list_4:
        i += 1
        continue

    if list_1[i] in list_2:
        list_4.append(list_1[i])
    i += 1

print(list_4)
