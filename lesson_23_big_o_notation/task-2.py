# Determine the complexity of one of the existing tasks (task-3 from lesson_o5).

import random

input_string = input('Enter a string: ')
original_string = input_string  # O(1)

for i in range(5):  # O(5)
    new_string = ""  # O(1)
    input_string = original_string  # O(1)
    while len(input_string) > 0: # O(n)
        index = random.randint(0, len(input_string) - 1)  # O(1)
        new_string = new_string + input_string[index]  # O(n)
        input_string = input_string[0:index] + input_string[index + 1:]  # O(n)

    print(f"{new_string}")  # O(1)

    # O(1) + O(5)*(O(1) + O(1) + O(n)*(O(1) + O(n) + O(n)) + O(1)) = O(1) + O(5) * O(2 + n*(1+ 2n) + O(5) =
    # = O(6) + O(10 + 5n + 10n^2) = O(n^2)
