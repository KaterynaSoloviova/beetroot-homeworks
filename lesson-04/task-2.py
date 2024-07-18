# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

phone_number = input('Enter a phone number: ')
length = len(phone_number)

if length == 10:
    if phone_number.isdigit():
        print("Your phone number is valid")
    else:
        print("Your phone number is invalid. It should content only numerical characters")
else:
    print("Your phone number is invalid. It should content 10 characters")
