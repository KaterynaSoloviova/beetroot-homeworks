# Task 1
# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def push(self, item: str | int) -> None:
        self.items.append(item)

    def pop(self) -> str | int:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self) -> str | int:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


def reverse_sequence(sequence: str) -> str:
    stack = Stack()
    for char in sequence:
        stack.push(char)
    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()
    return reversed_sequence


if __name__ == "__main__":
    text = input("Enter a sequence of characters: ")
    print(f"Reversed sequence: {reverse_sequence(text)}")
