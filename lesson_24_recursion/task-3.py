# All tasks should be solved using recursion

# Task 3
import pytest


def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")

    if a == 0 or n == 0:
        return 0

    else:
        return a + mult(a, n - 1)


# print(mult(2, 4))  # Output: 8
# print(mult(2, 0))  # Output: 0
# print(mult(2, -4))  # Raises ValueError


def test_numbers_equal_to_zero():
    assert mult(2, 0) == 0


def test_negative_numbers():
    with pytest.raises(ValueError) as ctx:
        mult(2, -4)
    assert str(ctx.value) == "This function works only with positive integers"


def test_recursive_case():
    assert mult(2, 4) == 8
