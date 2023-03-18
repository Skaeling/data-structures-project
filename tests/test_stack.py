"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack, Node
import unittest


class TestStack(unittest.TestCase):

    def test_stack_str(self):
        st = Stack()
        st.push('first')
        st.push('second')
        st.push('third')
        self.assertEqual(str(st), "Stack (third)")

    def test_node(self):
        n1 = Node(10, None)
        n2 = Node('b', n1)
        self.assertIsNone(n1.next_node)
        self.assertIs(n1, n2.next_node)

    def test_stack_push(self):
        st = Stack()
        st.push('first')
        st.push('second')
        st.push('third')
        self.assertIs(st.top.data, "third")

    def test_stack_pop(self):
        st = Stack()
        st.push('first')
        node_1 = st.top
        st.push('second')
        node_2 = st.top
        self.assertIs(st.pop(), node_2.data)
        self.assertIs(st.pop(), node_1.data)

