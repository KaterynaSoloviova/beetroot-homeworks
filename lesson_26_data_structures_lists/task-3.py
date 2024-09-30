# Task 3
# Implement a queue using a singly linked list.

from task1 import Node


class Queue:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, data: str | int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def dequeue(self) -> Node:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        current_node = self.head
        previous_node = None
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        if previous_node is not None:
            previous_node.next = None
        else:
            self.head = None
        return current_node

    def size(self) -> int:
        index = 0
        current_node = self.head
        while current_node is not None:
            index += 1
            current_node = current_node.next
        return index


def test_queue():
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')

    assert queue.is_empty() is False
    assert queue.size() == 2
    assert queue.dequeue().data == 'a'
    assert queue.dequeue().data == 'b'
    assert queue.is_empty() is True
