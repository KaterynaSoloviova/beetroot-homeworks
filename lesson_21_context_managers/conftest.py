import pytest

from task1 import OpenFileManager


@pytest.fixture
def file_with_text():
    with OpenFileManager('text.txt', 'w') as file:
        file.write("I like Python!")
    with OpenFileManager('text.txt', 'r') as file:
        yield file


@pytest.fixture
def empty_file():
    with OpenFileManager('empty.txt', 'w') as file:
        file.write("")
    with OpenFileManager('empty.txt', 'r') as file:
        yield file


@pytest.fixture
def multiple_spaces():
    with OpenFileManager('mult_spaces.txt', 'w') as file:
        file.write("a   b")
    with OpenFileManager('mult_spaces.txt', 'r') as file:
        yield file


@pytest.fixture
def strings_with_numbers():
    with OpenFileManager('numbers_strings.txt', 'w') as file:
        file.write("56")
    with OpenFileManager('numbers_strings.txt', 'r') as file:
        yield file
