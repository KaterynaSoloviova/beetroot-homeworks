# Task 3
# Implement in (__contains__) and (__len__) methods for HashTable

class Node:
    def __init__(self, key: int | str, value: int | str) -> None:
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key: int | str) -> int:
        return hash(key) % self.capacity

    def insert(self, key: int | str, value: int | str) -> None:
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
            return
        else:
            current = self.table[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def __contains__(self, key: int | str) -> bool:
        index = self._hash(key)

        if self.table[index] is None:
            return False
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False

    def __len__(self) -> int:
        return self.size


def test_contains_true():
    table = HashTable(4)

    table.insert(2, 1)
    table.insert(3, 99)
    table.insert(4, "Lyu")
    table.insert("yu", 8)

    res = table.__contains__(4)

    assert res is True


def test_contains_false():
    table = HashTable(4)

    table.insert(2, 1)
    table.insert(3, 99)
    table.insert(4, "Lyu")
    table.insert("yu", 8)

    res = table.__contains__(1)

    assert res is False


def test_contains_false():
    table = HashTable(4)

    table.insert(2, 1)
    table.insert(3, 99)
    table.insert(4, "Lyu")
    table.insert("yu", 8)

    res = 1 in table

    assert res is False


def test_len():
    table = HashTable(4)

    table.insert(2, 1)
    table.insert(3, 99)
    table.insert(4, "Lyu")
    table.insert("yu", 8)

    res = table.__len__()

    assert res == 4


def test_len():
    table = HashTable(4)

    table.insert(2, 1)
    table.insert(3, 99)
    table.insert(4, "Lyu")
    table.insert("yu", 8)

    res = len(table)

    assert res == 4
