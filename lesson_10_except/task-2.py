# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
# the value of squared a divided by b, construct a try-except block which raises an exception if the two values given
# by the input function were not numbers, and if value b was zero (cannot divide by zero).

def number_in_squer_division():
    try:
        a = float(input("Please enter the number a: "))
        b = float(input("Please enter the number b: "))
        return a ** 2 / b

    except ValueError:
        return "Invalid input. Please enter numeric values"
    except ZeroDivisionError:
        return "It is not possible to divide by zero"


print(number_in_squer_division())
