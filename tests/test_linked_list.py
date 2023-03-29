from src.linked_list import Node, LinkedList
import unittest


class TestNode(unittest.TestCase):
    def test_node(self):
        n1 = Node(10, None)
        n2 = Node('b', n1)
        self.assertIsNone(n1.next_node)
        self.assertIs(n1, n2.next_node)


class TestLinkedList(unittest.TestCase):
    def test_init_llist(self):
        new_llist = LinkedList()
        self.assertIsNone(new_llist.head)
        self.assertIsNone(new_llist.next_node)

    def test_insert_head(self):
        new_llist = LinkedList()
        new_llist.insert_beginning({'index': 'first'})
        new_llist.insert_beginning({'index': 'second'})
        new_llist.insert_beginning({'index': 'last'})
        self.assertEqual(new_llist.__str__().split(" -> ")[0], "{'index': 'last'}")

    def test_insert_tail(self):
        new_llist = LinkedList()
        new_llist.insert_at_end({'index': 'first'})
        new_llist.insert_at_end({'index': 'second'})
        new_llist.insert_at_end({'index': 'last'})
        self.assertEqual(new_llist.__str__().split(" -> ")[0], "{'index': 'first'}")
