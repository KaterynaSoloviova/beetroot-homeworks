# Task 3
# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class MyIterable:
    def __init__(self, data) -> None:
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]


my_iterable = MyIterable([7, 8, 23, 40, 110])

for item in my_iterable:
    print(item)
    print(my_iterable[0])
    print(my_iterable[3])
    print(my_iterable[1:5])
