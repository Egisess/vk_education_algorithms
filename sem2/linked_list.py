class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, data=[]):
        # Сторожевые узлы
        self.dummy_head = Node()  # Фиктивная голова
        self.tail = self.dummy_head  # Изначально хвост указывает на фиктивную голову
        self.size = 0

        self.fill_from_array(data)

    def fill_from_array(self, data):
        for num in data:
            self.insert_at_end(num)
        return self

    def make_cycle(self, data):
        if not self.dummy_head.next:
            raise IndexError

        for cycle in data:
            left = self.dummy_head
            right = self.dummy_head

            if cycle[0] > cycle[1] or max(cycle) > self.size - 1:
                raise IndexError

            for i in range(0, cycle[0] + 1):
                left = left.next
            for j in range(0, cycle[1] + 1):
                right = right.next

            right.next = left
            return self

    def insert_at_beginning(self, data):
        """Вставка в начало за O(1)"""
        new_node = Node(data)
        new_node.next = self.dummy_head.next  # Привязываем новый узел к текущему первому элементу
        self.dummy_head.next = new_node  # Фиктивная голова теперь указывает на новый узел

        # Если список был пуст, обновляем хвост
        if self.tail == self.dummy_head:
            self.tail = new_node
        self.size += 1

        return self

    def insert_at_end(self, data):
        """Вставка в конец за O(1)"""
        new_node = Node(data)
        self.tail.next = new_node  # Старый хвост ссылается на новый узел
        self.tail = new_node  # Новый узел становится хвостом
        self.size += 1

        return self

    def __str__(self):
        current = self.dummy_head.next
        string = []
        while current:
            string.append(str(current.data))
            current = current.next
        if not string:
            return 'None'
        return ' -> '.join(string)

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False

        current_self = self.dummy_head.next
        current_other = other.dummy_head.next

        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next

        return current_self is None and current_other is None

    def get_i_th_node(self, n):
        cur = self.dummy_head
        i = n
        while cur.next and i >= 0:
            cur = cur.next
            i -= 1
        return cur
