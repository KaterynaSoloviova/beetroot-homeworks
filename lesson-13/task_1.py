# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def number_local_variables(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")

print(number_local_variables.__code__.co_nlocals)