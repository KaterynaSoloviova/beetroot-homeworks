# All tasks should be solved using recursion

# Task 4

def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str

    return reverse(input_str[1:]) + input_str[0]


print(reverse("hello"))  # Output: "olleh"
print(reverse("o"))  # Output: "o"


def test_one_character_in_the_string():
    assert reverse("o") == "o"


def test_word_case():
    assert reverse("hello") == "olleh"


def test_empty_string():
    assert reverse("") == ""
