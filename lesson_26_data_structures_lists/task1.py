# Task 1
# Extend UnorderedList
# Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two
# parameters start and stop, and return a copy of the list starting at the position and going up to but not including
# the stop position.

import pytest


class Node:
    def __init__(self, init_data: str | int) -> None:
        self.__data = init_data
        self.__next = None

    @property
    def data(self) -> str | int:
        return self.__data

    @property
    def next(self) -> 'Node':
        return self.__next

    @data.setter
    def data(self, new_data: str | int) -> None:
        self.__data = new_data

    @next.setter
    def next(self, new_next: 'Node') -> None:
        self.__next = new_next


class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: int | str) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def index(self, data: int | str) -> int:
        if self.is_empty():
            return -1
        else:
            index = 0
            current_node = self.head
            while current_node is not None:
                if current_node.data == data:
                    return index
                index += 1
                current_node = current_node.next
            return -1

    def pop(self) -> Node:
        if self.is_empty():
            raise IndexError("List is empty")
        else:
            current_node = self.head
            previous_node = None
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None
            return current_node

    def insert(self, data: str | int, pos: int) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return None
        index = 0
        current_node = self.head
        found = False
        while current_node is not None:
            current_node = current_node.next
            index += 1
            if index == pos - 1:
                found = True
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                break
        if not found:
            raise IndexError("Position is out of range")

    def slice(self, start: int, stop: int) -> 'UnorderedList':
        if self.is_empty():
            raise ValueError("List is empty")
        new_list = UnorderedList()
        index = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            index += 1
            if start <= index < stop:
                new_list.append(current_node.data)
            elif index == stop:
                break
        return new_list


def test_is_empty_return_true():
    list = UnorderedList()

    res = list.is_empty()

    assert res is True


def test_is_empty_return_false():
    list = UnorderedList()
    list.append(99)

    res = list.is_empty()

    assert res is False


def test_append_one_node():
    list = UnorderedList()
    assert list.head is None

    list.append(13)

    assert list.head is not None
    assert list.head.data == 13


def test_append_two_nodes():
    list = UnorderedList()
    assert list.head is None

    list.append(13)
    list.append(14)

    assert list.head is not None
    assert list.head.data == 13
    assert list.head.next.data == 14


def test_index_empty_list():
    list = UnorderedList()

    res = list.index(2)

    assert res == -1


def test_index_with_elements():
    list = UnorderedList()
    list.append(56)
    list.append(23)

    res = list.index(23)

    assert res == 1


def test_index_with_not_excist_element():
    list = UnorderedList()
    list.append(56)
    list.append(23)

    res = list.index(32)

    assert res == -1


def test_pop_empty_list():
    list = UnorderedList()
    with pytest.raises(IndexError) as ctx:
        list.pop()
    assert str(ctx.value) == "List is empty"


def test_pop_list_with_elements():
    list = UnorderedList()
    list.append(36)
    list.append(15)

    res = list.pop()

    assert res.data == 15
    assert list.head.data == 36
    assert list.head.next is None


def test_insert():
    list = UnorderedList()
    list.append(88)
    list.append(35)
    list.append(40)

    list.insert(4, 2)

    assert list.head.data == 88
    assert list.head.next.data == 35
    assert list.head.next.next.data == 4
    assert list.head.next.next.next.data == 40


def test_insert_empty_list():
    list = UnorderedList()

    list.insert(86, 0)

    assert list.head.data == 86
    assert list.head.next is None


def test_insert_not_excist_pos():
    list = UnorderedList()
    list.append(35)
    list.append(37)

    with pytest.raises(IndexError) as ctx:
        list.insert(86, 4)

    assert str(ctx.value) == "Position is out of range"
    assert list.head.data == 35
    assert list.head.next.data == 37
    assert list.head.next.next is None


def test_slice_empty_list():
    list = UnorderedList()

    with pytest.raises(ValueError) as ctx:
        list.slice(1, 3)

    assert str(ctx.value) == "List is empty"


def test_slice():
    list = UnorderedList()
    list.append(5)
    list.append("8")
    list.append(65)
    list.append(11)

    res = list.slice(1, 3)

    assert res.head.data == "8"
    assert res.head.next.data == 65
    assert res.head.next.next is None

    list.head.next.data = "new"
    assert res.head.next.data == 65
