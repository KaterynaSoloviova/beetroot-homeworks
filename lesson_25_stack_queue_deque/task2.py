# Task 2
# Write a program that reads in a sequence of characters, and determines whether it's parentheses,
# braces, and curly brackets are "balanced."
from task1 import Stack


def is_balanced(sequence: str) -> bool:
    stack = Stack()
    matching_brackets = {'(': ')', '{': '}', '[': ']'}

    for char in sequence:
        if char in matching_brackets:
            stack.push(char)
        elif char in matching_brackets.values():
            if stack.is_empty() or matching_brackets[stack.pop()] != char:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    text = input("Enter a sequence of characters with parentheses, braces, and curly brackets: ")
    print(f"The statement, that presented brackets are balanced, is: {is_balanced(text)}")
