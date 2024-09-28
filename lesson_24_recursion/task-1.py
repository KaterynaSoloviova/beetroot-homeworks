# All tasks should be solved using recursion

# Task 1

import pytest
from typing import Optional, Union


def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    if exp == 0:
        return 1  # Base case: x^0 is 1
    elif exp == 1:
        return x  # Base case: x^1 is x
    else:
        # Recursive case: x^exp = x * x^(exp-1)
        return x * to_power(x, exp - 1)


# print(to_power(2, 3))  # Output: 8
# print(to_power(3.5, 2))  # Output: 12.25
# print(to_power(2, -1))  # Raises ValueError

def test_power_with_exp_3():
    assert to_power(2, 3) == 8


def test_power_with_float_x():
    assert to_power(3.5, 2) == 12.25


def test_power_with_negative_exp():
    with pytest.raises(ValueError) as ctx:
        to_power(2, -1)
    assert str(ctx.value) == "This function works only with exp > 0."
