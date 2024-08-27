# Task 1
# Create your own implementation of a built-in function enumerate, named with_index(), which takes two parameters:
# iterable and start, default is 0. Tips: see the documentation for the enumerate function.

def with_index(iterable, start=0):
    i = start

    for item in iterable:
        yield i, item
        i += 1


for index, value in with_index(['a', 'b', 'c'], start=1):
    print(index, value, sep=':', end=', ')

print()
for index, char in with_index('I like Python', start=5):
    print(index, char, sep=':', end=', ')
