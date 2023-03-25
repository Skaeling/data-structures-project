
class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        current_node = Node(data)
        if not self.head and not self.tail:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next_node = current_node
            self.tail = current_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if not self.head:
            return None
        else:
            data = self.head.data
            self.head = self.head.next_node
            return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        head = self.head
        result = []
        while head:
            result.append(head.data)
            head = head.next_node
        return '\n'.join(result)
