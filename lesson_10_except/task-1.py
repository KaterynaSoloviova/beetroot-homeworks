# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
# that calls oops inside a try/except statement to catch the error. What happens if you change oops to raise KeyError
# instead of IndexError?

def oops():
    raise IndexError("This is an IndexError")


def handle_oops():
    try:
        oops()
    except (IndexError, KeyError) as e:
        return f"We have an expection: {e}"


print(handle_oops())


def oops():
    raise KeyError("This is a KeyError")


print(handle_oops())
