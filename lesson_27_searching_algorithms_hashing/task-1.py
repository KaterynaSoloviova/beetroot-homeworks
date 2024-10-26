# Task 1
# Implement binary search using recursion.

def binary_search(arr: list, low: int, high: int, value: int) -> int:
    mid = (low + high) // 2
    if low > high:
        return -1
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return binary_search(arr, mid + 1, high, value)
    else:
        return binary_search(arr, low, mid - 1, value)


def test_binary_search_out_of_range_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = binary_search(arr, 0, len(arr) - 1, 101)

    assert res == -1


def test_binary_search_first_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = binary_search(arr, 0, len(arr) - 1, 10)

    assert res == 0


def test_binary_search_last_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = binary_search(arr, 0, len(arr) - 1, 100)

    assert res == 10


def test_binary_search_middle_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = binary_search(arr, 0, len(arr) - 1, 80)

    assert res == 6


def test_binary_search_not_excist_element():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    res = binary_search(arr, 0, len(arr) - 1, 56)

    assert res == -1
