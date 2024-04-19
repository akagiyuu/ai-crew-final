from collections.abc import Iterator
from typing import Generic, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.item = data
        self.next: Node[T] | None = None
        self.prev: Node[T] | None = None

    def __str__(self) -> str:
        return f"{self.item}"


"""
Double-ended queue
"""


class VecDequeue(Generic[T]):
    def __init__(self) -> None:
        self.__front: Node[T] | None = None
        self.__back: Node[T] | None = None
        self.__length: int = 0

    def __iter__(self) -> Iterator[T]:
        """
        >>> vec = VecDequeue()
        >>> vec.push_front('b')
        >>> vec.push_front('a')
        >>> vec.push_back('c')
        >>> tuple(vec)
        ('a', 'b', 'c')
        """
        node = self.__front
        while node is not None:
            yield node.item
            node = node.next

    def __str__(self) -> str:
        """
        >>> vec = VecDequeue()
        >>> str(vec)
        '[]'
        >>> vec.push_back('a')
        >>> vec.push_back('b')
        >>> vec.push_back('c')
        >>> str(vec)
        '[a, b, c]'
        """
        if self.is_empty():
            return "[]"

        result = f"[{self.__front}"
        node = self.__front.next
        while node is not None:
            result += f", {node}"
            node = node.next
        result += "]"
        return result

    def __len__(self) -> int:
        """
        >>> vec = VecDequeue()
        >>> for i in range(0, 5):
        ...     vec.insert(i, i + 1)
        >>> len(vec)
        5
        """
        return self.__length

    def is_empty(self) -> bool:
        return self.__length == 0

    def front(self) -> Node[T] | None:
        return self.__front

    def back(self) -> Node[T] | None:
        return self.__back

    def push_back(self, item: T) -> None:
        new_node = Node(item)
        new_node.prev = self.__back
        if not self.is_empty():
            self.__back.next = new_node

        self.__back = new_node
        if self.is_empty():
            self.__front = new_node
        self.__length += 1

    def push_front(self, item: T) -> None:
        new_node = Node(item)
        new_node.next = self.__front
        if not self.is_empty():
            self.__front.prev = new_node

        self.__front = new_node
        if self.is_empty():
            self.__back = new_node
        self.__length += 1

    def pop_front(self) -> T:
        if self.__length == 0:
            raise IndexError("Index out of range")

        item = self.__front.item
        if self.__length == 1:
            self.__back = None
            self.__front = None
        else:
            self.__front = self.__front.next
            self.__front.prev = None
        self.__length -= 1
        return item

    def pop_back(self) -> T:
        if self.__length == 0:
            raise IndexError("Index out of range")

        item = self.__back.item
        if self.__length == 1:
            self.__back = None
            self.__front = None
        else:
            self.__back = self.__back.prev
            self.__back.next = None
        self.__length -= 1
        return item

    def __get(self, index: int) -> Node[T]:
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of range")

        node = self.__front
        for _ in range(0, index):
            node = node.next
        return node

    def __getitem__(self, index: int) -> T:
        return self.__get(index).item

    def __setitem__(self, index: int, item: T) -> None:
        self.__get(index).item = item

    def insert(self, index: int, item: T) -> None:
        """
        >>> vec = VecDequeue()
        >>> vec.insert(-1, 666)
        Traceback (most recent call last):
            ....
        IndexError: Index out of range
        >>> vec.insert(1, 666)
        Traceback (most recent call last):
            ....
        IndexError: Index out of range
        >>> vec.insert(0, 2)
        >>> vec.insert(0, 1)
        >>> vec.insert(2, 4)
        >>> vec.insert(2, 3)
        >>> str(vec)
        '[1, 2, 3, 4]'
        >>> vec.insert(5, 5)
        Traceback (most recent call last):
            ....
        IndexError: Index out of range
        """
        if index == 0:
            self.push_front(item)
            return
        if index == self.__length:
            self.push_back(item)
            return

        # current not is not front
        current_node = self.__get(index)
        new_node = Node(item)
        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev.next = new_node
        current_node.prev = new_node
        self.__length += 1

    def remove(self, index: int) -> T:
        """
        >>> vec = VecDequeue()
        >>> vec.remove(0)
        Traceback (most recent call last):
            ....
        IndexError: Index out of range
        >>> for i in range(0, 5):
        ...     vec.insert(i, i + 1)
        >>> vec.remove(0) == 1
        True
        >>> vec.remove(3) == 5
        True
        >>> vec.remove(1) == 3
        True
        >>> str(vec)
        '[2, 4]'
        >>> vec.remove(2)
        Traceback (most recent call last):
            ....
        IndexError: Index out of range
        """
        if index == 0:
            return self.pop_front()
        if index == self.__length - 1:
            return self.pop_back()

        # node is not front or back and length >= 3
        node = self.__get(index)
        node.next.prev = node.prev
        node.prev.next = node.next
        self.__length -= 1
        return node.item
