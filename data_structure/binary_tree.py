from collections.abc import Iterator
from typing import Generic, TypeVar
from .vec_dequeue import VecDequeue


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.item = data
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None

    def __str__(self) -> str:
        return f"{self.item}"

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def inorder_traversal(self) -> Iterator[T]:
        if self.left is not None:
            yield from self.left
        yield self.item
        if self.right is not None:
            yield from self.right

    def preorder_traversal(self) -> Iterator[T]:
        yield self.item
        if self.left is not None:
            yield from self.left.preorder_traversal()
        if self.right is not None:
            yield from self.right.preorder_traversal()

    def postorder_traversal(self) -> Iterator[T]:
        if self.left is not None:
            yield from self.left.postorder_traversal()
        if self.right is not None:
            yield from self.right.postorder_traversal()
        yield self.item

    def __iter__(self) -> Iterator[T]:
        return self.inorder_traversal()

    def insert(self, item: T) -> None:
        if item == self.item:
            return

        if item > self.item:
            if self.right is None:
                self.right = Node(item)
                return
            self.right.insert(item)
            return

        if item < self.item:
            if self.left is None:
                self.left = Node(item)
                return
            self.left.insert(item)
            return

    def depth(self) -> int:
        depth = 0

        if self.left is not None:
            depth = max(depth, self.left.depth())
        if self.right is not None:
            depth = max(depth, self.right.depth())
        depth += 1

        return depth


class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        self.__root: Node[T] | None = None

    def __iter__(self) -> Iterator[T]:
        """
        >>> tree = BinaryTree()
        >>> tree.insert(2)
        >>> tree.insert(1)
        >>> tree.insert(3)
        >>> tree.insert(0)
        >>> list(tree)
        [0, 1, 2, 3]
        """
        if self.__root is None:
            return iter(())
        return iter(self.__root)

    def __str__(self) -> str:
        """
        >>> tree = BinaryTree()
        >>> tree.insert(2)
        >>> tree.insert(1)
        >>> tree.insert(3)
        >>> str(tree)
        '[1, 2, 3]'
        """
        result = "["
        is_front = True
        for item in self:
            if is_front:
                result += str(item)
                is_front = False
                continue
            result += f", {item}"
        result += "]"
        return result

    def __len__(self) -> int:
        """
        >>> tree = BinaryTree()
        >>> tree.insert(2)
        >>> tree.insert(1)
        >>> tree.insert(3)
        >>> len(tree)
        3
        """
        if self.__root is None:
            return 0
        return len(self.__root)

    def __contains__(self, item: T) -> bool:
        """
        >>> tree = BinaryTree()
        >>> tree.insert(2)
        >>> tree.insert(1)
        >>> tree.insert(3)
        >>> 3 in tree
        True
        """
        for x in self:
            if x == item:
                return True
        return False

    def depth(self) -> int:
        """
        >>> tree = BinaryTree()
        >>> tree.insert(2)
        >>> tree.insert(1)
        >>> tree.insert(3)
        >>> tree.depth()
        2
        """
        if self.__root is None:
            return 0
        return self.__root.depth()

    def insert(self, item: T) -> None:
        if self.__root is None:
            self.__root = Node(item)
            return
        self.__root.insert(item)

    def inorder_traversal(self) -> Iterator[T]:
        if self.__root is None:
            return iter(())
        return self.__root.inorder_traversal()

    def preorder_traversal(self) -> Iterator[T]:
        if self.__root is None:
            return iter(())
        return self.__root.preorder_traversal()

    def postorder_traversal(self) -> Iterator[T]:
        if self.__root is None:
            return iter(())
        return self.__root.postorder_traversal()

    def bfs(self) -> Iterator[T]:
        """
        >>> tree = BinaryTree()
        >>> tree.insert(2)
        >>> tree.insert(1)
        >>> tree.insert(3)
        >>> tree.insert(0)
        >>> list(tree.bfs())
        [2, 1, 3, 0]
        """
        if self.__root is None:
            return iter(())
        queue = VecDequeue[Node[T]]()
        queue.push_back(self.__root)
        while not queue.is_empty():
            current = queue.pop_front()
            yield current.item
            if current.left is not None:
                queue.push_back(current.left)
            if current.right is not None:
                queue.push_back(current.right)
