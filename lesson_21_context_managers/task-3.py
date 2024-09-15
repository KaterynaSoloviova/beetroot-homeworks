# Task 3 (Optional)
# Pytest fixtures with context manager
# Create a simple function, which performs any logic of your choice with text data, which it obtains from a file object,
# passed to this function ( def test(file_obj) ).
# Create a test case for this function using pytest library (Full pytest documentation).
# Create pytest fixture, which uses your implementation of the context manager to return a file object, which could
# be used inside your function.

from io import TextIOWrapper


def words_count(file_obj: TextIOWrapper) -> int:
    text = file_obj.read()
    if text == "":
        return 0
    words = text.split(" ")
    counter = 0
    for word in words:
        if word != "":
            counter += 1
    return counter


def test_words_number(file_with_text):
    res = words_count(file_with_text)
    assert res == 3


def test_empty_file(empty_file):
    res = words_count(empty_file)
    assert res == 0


def test_strings_with_multiple_spaces(multiple_spaces):
    res = words_count(multiple_spaces)
    assert res == 2


def test_strings_with_numbers(strings_with_numbers):
    res = words_count(strings_with_numbers)
    assert res == 1
