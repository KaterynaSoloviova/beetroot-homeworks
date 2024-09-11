# Task 2
# Create your own implementation of a built-in function range(), named in_range(), which takes three parameters:
# start, end, and optional step. Tips: See the documentation for range() function

def in_range(start: int, end: int = None, step: int = 1):
    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("In the function in_range() step argument must not be zero")

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step


print(list(in_range(5)))
print(list(in_range(1, 5)))
print(list(in_range(5, 0, -1)))
print(list(in_range(0, 10, 2)))
