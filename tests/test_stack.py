"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src import stack
import unittest

class TestStack(unittest.TestCase):
    def test_node(self):
        n1 = stack.Node(10, None)
        n2 = stack.Node('b', n1)
        self.assertIsNone(n1.next_node)
        self.assertIs(n1, n2.next_node)

    def test_stack(self):
        st = stack.Stack()
        st.push('first')
        st.push('second')
        st.push('third')
        self.assertIs(st.top.data, "third")
