# Task 3
# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order. Consider the case in which the element is not
# found - raise ValueError with proper info Message

# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order. Consider the case in which the element is not
# found - raise ValueError with proper info Message

import pytest
from task1 import Stack


class StackExtended(Stack):
    def get_from_stack(self, e: str | int) -> str | int:
        temp = []
        found = False
        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            else:
                temp.append(item)
        while len(temp) > 0:
            self.push(temp.pop())
        if not found:
            raise ValueError(f"Element {e} not found in the stack.")
        return e


def test_get_from_stack_success():
    stack = StackExtended()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(10)

    res = stack.get_from_stack(7)

    assert res == 7
    assert stack.items == [5, 6, 10]


def test_get_from_stack_fail():
    stack = StackExtended()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(10)

    with pytest.raises(ValueError) as ctx:
        stack.get_from_stack(2)

    assert str(ctx.value) == "Element 2 not found in the stack."


class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def enqueue(self, item: str | int) -> None:
        self.items.append(item)

    def dequeue(self) -> str | int:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)

    def get_from_queue(self, e):
        temp = []
        found = False
        while not self.is_empty():
            item = self.dequeue()
            if item == e and not found:
                found = True
            else:
                temp.append(item)
        for item in temp:
            self.enqueue(item)
        if not found:
            raise ValueError(f"Element {e} not found in the queue.")
        return e


def test_get_from_queue_successes():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    res = q.get_from_queue(2)
    assert res == 2
    assert q.items == [1, 3, 4]

def test_get_from_queue_successes_2():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(2)

    res = q.get_from_queue(2)

    assert res == 2
    assert q.items == [1, 3, 4, 2]

def test_get_from_queue_fail():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(2)

    with pytest.raises(ValueError) as ctx:
        q.get_from_queue(6)

    assert str(ctx.value) == 'Element 6 not found in the queue.'



