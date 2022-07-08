from typing import Any, Optional

class Node:

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        next_node_repr = f"DoubleLinkedNode({self.next.value})" if self.next else "None"
        prev_node_repr = f"DoubleLinkedNode({self.prev.value})" if self.prev else "None"
        return f"DoubleLinkedNode({self.value}, {prev_node_repr}, {next_node_repr})"

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self._prev = prev


if __name__ == "__main__":
    first_node = Node(1)
    second_node = Node(2)

    first_node.next = second_node

    print(repr(first_node))
    print(repr(second_node))
    print(repr(first_node.next))
