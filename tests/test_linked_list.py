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

    def test_to_list(self):
        new_llist = LinkedList()
        new_llist.insert_at_end({'index': 'first'})
        new_llist.insert_at_end({'index': 'second'})
        data_list = new_llist.to_list()
        self.assertEqual(data_list[0], {'index': 'first'})

    def test_get_data(self):
        new_llist = LinkedList()
        new_llist.insert_beginning({'id': "1"})
        data = new_llist.get_data_by_id(1)
        self.assertIsNone(data)
        new_llist.insert_at_end({'id': 2})
        data = new_llist.get_data_by_id(2)
        self.assertEqual(data, {'id': 2})

