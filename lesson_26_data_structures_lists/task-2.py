# Task 2
# Implement a stack using a singly linked list.

from task1 import Node


class Stack:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data: str | int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> Node:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        top_node = self.head
        self.head = top_node.next
        return top_node

    def peek(self) -> Node:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        top_node = self.head
        return top_node

    def size(self) -> int:
        index = 0
        current_node = self.head
        while current_node is not None:
            index += 1
            current_node = current_node.next
        return index


def test_stack():
    stack = Stack()
    stack.push('a')
    stack.push('b')

    assert stack.is_empty() is False
    assert stack.size() == 2
    assert stack.peek().data == 'b'
    assert stack.size() == 2
    assert stack.pop().data == 'b'
    assert stack.pop().data == 'a'
    assert stack.size() == 0
    assert stack.is_empty() is True
