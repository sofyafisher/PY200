import unittest

from node import Node
from node import DoubleLinkedNode
from task import LinkedList
from task import DoubleLinkedList


class TestCase2(unittest.TestCase):
    def test_append(self):
        list_ = LinkedList([1, 2, 3])
        list_.append(4)
        msg = "Значение не было добавлено в конец последовательности"
        self.assertEqual(str(list_._tail), str(Node(4, None)), msg)

    def test_linked_nodes(self):
        first_node = Node("first_node")
        second_node = Node("second_node")
        LinkedList.linked_nodes(first_node, second_node)
        msg = "Узлы связаны некорректно"
        self.assertIs(first_node.next, second_node, msg)




