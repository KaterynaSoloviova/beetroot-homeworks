# All tasks should be solved using recursion

# Task 2


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 0:
        return False

    if index >= len(looking_str) // 2:  # base case
        return True

    if looking_str[index] != looking_str[-index - 1]:
        return False

    return is_palindrome(looking_str, index + 1)  # recursive case


# print(is_palindrome('mom'))  # Output: True
# print(is_palindrome('sassas'))  # Output: True
# print(is_palindrome('hello'))  # Output: False


def test_palindrome_with_odd_number_characters():
    assert is_palindrome('mom') is True


def test_palindrome_with_even_number_characters():
    assert is_palindrome('sassas') is True


def test_not_palindrome():
    assert is_palindrome('hello') is False


def test_palindrome_with_one_character():
    assert is_palindrome('m') is True


def test_not_palindrome_with_two_characters():
    assert is_palindrome('mn') is False


def test_not_palindrome_with_empty_string():
    assert is_palindrome('') is False
