# Task 1

# Make a program that has your name and the current day of the week stored as separate variables and then prints
# a message like this:
# "Good day <name>! <day> is a perfect day to learn some python."
# Note that <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods for constructing result string.

name = "Yurii"
day = "Monday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")

print("Good day %s! %s is a perfect day to learn some python." % (name, day))

s = "Good day {}! {} is a perfect day to learn some python."
print(s.format(name, day))

print("Good day {0}! {1} is a perfect day to learn some python.".format(name, day))

res = f"Good day {name}! {day} is a perfect day to learn some python."
print(res)
