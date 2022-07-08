import unittest

from node import Node
from node import DoubleLinkedNode


class TestCase(unittest.TestCase):

    def test_repr_node_without_next(self):
        node = Node("node_without_next")
        msg = "Значение представления __repr__ некорректно для узла без следующего узла. "
        self.assertEqual(repr(node), "Node(node_without_next, None)", msg)

    def test_repr_node_with_next(self):
        first_node = Node(1, Node(2))
        msg = "Значение представления __repr__ некорректно для случая когда установлен следующий узел . "
        self.assertEqual(repr(first_node), "Node(1, Node(2))", msg)

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node("correct_node"))

        with self.assertRaises(TypeError):
            Node.is_valid("incorrect_type")

    def test_repr_node_with_next_and_prev(self):
        second_node = DoubleLinkedNode(2, DoubleLinkedNode(1), DoubleLinkedNode(3))
        msg = "Значение представления __repr__ некорректно для случая когда установлен следующий узел . "
        self.assertEqual(repr(second_node), "DoubleLinkedNode(2, DoubleLinkedNode(1), DoubleLinkedNode(3))", msg)