"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue
import unittest
from types import NoneType


class TestQueue(unittest.TestCase):

    def test_queue_str(self):
        qu = Queue()
        qu.enqueue('first')
        qu.enqueue('second')
        qu.enqueue('third')
        self.assertEqual(str(qu), "first\nsecond\nthird")

    def test_queue_enqueue(self):
        qu = Queue()
        qu.enqueue('first')
        qu.enqueue('second')
        qu.enqueue('third')
        self.assertIs(qu.tail.data, "third")
        self.assertIsInstance(qu.tail.next_node, NoneType)
