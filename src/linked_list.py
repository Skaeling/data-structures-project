class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.next_node = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, self.head)
        if self.head is None:
            self.head = node
        else:
            self.head = node
            self.next_node = self.head.data

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, self.head)
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = Node(data, current.next_node)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return f'{ll_string}'

    def to_list(self) -> list:
        """Возвращает список с данными,
        содержащимися в односвязном списке `LinkedList`"""
        data_list = []
        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, data) -> dict:
        """Возвращает первый найденный в `LinkedList` словарь
        с ключом 'id', значение которого равно переданному в метод значению."""
        node = self.head
        for node.data in self.to_list():
            try:
                if data == node.data['id']:
                    return node.data

            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
