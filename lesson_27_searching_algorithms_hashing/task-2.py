# Task 2
# Read about the Fibonacci search and implement it using python. Explore its complexity and compare it to sequential,
# binary searches.

def fibonacci_search(arr: list, value: int) -> int:
    n = len(arr)
    if n == 0:
        return -1

    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

    while fib3 < n:
        fib1, fib2 = fib2, fib3
        fib3 = fib1 + fib2

    offset = -1
    while fib3 > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < value:
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
            offset = i

        elif arr[i] > value:
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2

        else:
            return i

    if fib2 == 1 and (offset + 1) < n and arr[offset + 1] == value:
        return offset + 1
    else:
        return -1


def test_fibonacci_search_out_of_range_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = fibonacci_search(arr, 101)

    assert res == -1


def test_fibonacci_search_first_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = fibonacci_search(arr, 10)

    assert res == 0


def test_fibonacci_search_last_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = fibonacci_search(arr, 100)

    assert res == 10


def test_fibonacci_search_middle_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = fibonacci_search(arr, 80)

    assert res == 6


def test_fibonacci_search_not_excist_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = fibonacci_search(arr, 56)

    assert res == -1
