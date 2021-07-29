class Node:
    """
    An object containing data and reference to another node.
    Basic building block of LinkedList
    """
    def __init__(self, data=None, nxt=None):
        self.data = data
        self._nxt = nxt

    def nxt(self):
        return self._nxt

    def update_link(self, node):
        self._nxt = node

    def __repr__(self):
        return f'{self.data, self.nxt()}'


class LinkedList:
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
            self.size = 1
        else:
            self.head = None
            self.size = 0

    def is_empty(self):
        """
        Checks if linkedlist is empty
        :return: boolean
        """
        if self.head is None:
            return True
        else:
            return False

    def append(self, value):
        """
        inserts node at the end
        :param value:
        :return:
        """
        if self.is_empty():
            self.head = Node(value)
        else:
            end_node = self.tail()
            end_node.update_link(Node(value))
        self.size += 1

    def get(self, index):
        """
        returns data for node at index position
        :param index: positive integer
        :return: data
        """
        current = self.get_node(index)
        return current.data

    def get_node(self, index):
        """
        returns node at index position
        :param index: positive integer
        :return: Node
        """
        if index < self.size:
            current = self.head
            for i in range(0, index):
                current = current.nxt()
            return current
        else:
            raise (IndexError("Invalid Index"))

    def insert(self, data, index):
        """
        Inserts data at index position
        :param data: data
        :param index: positive integer
        :return: None
        """
        new_node = Node(data)
        if index == 0:
            nxt = self.head
            self.head = new_node
        else:
            prev = self.get_node(index-1)
            nxt = prev.nxt()
            # put new node between prev and next
            prev.update_link(new_node)
        new_node.update_link(nxt)
        self.size += 1

    def prepend(self, value):
        self.insert(value, 0)

    def delete(self, index):
        """
        Delete node at position index
        :param index: positive integer
        :return: None
        """
        if index >= self.size:
            raise IndexError('Index invalid')
        elif index == 0:
            self.head = self.head.nxt()
        else:
            prev = self.get_node(index-1)
            to_del = prev.nxt()
            prev.update_link(to_del.nxt())
        self.size -= 1

    def tail(self):
        """
        last node in list
        :return:
        """
        if self.size == 0:
            return self.head
        return self.get_node(self.size - 1)

    def has(self, value):
        """
        Check if list has the value
        :param value:
        :return:
        """
        current = self.head
        for i in range(0,self.size):
            if current.data == value:
                return True
            current = current.nxt()
        return False

    def reverse(self, node):
        """
        :param node: head node of the list
        :return:
        """
        if node.nxt():
            next_ = self.reverse(node.nxt())
            next_.update_link(node)
            return node
        else:  # base condition
            self.head = node
            return node

    def __repr__(self):
        data_all = []
        current = self.head
        for i in range(0, self.size):
            data_all.append(current.data)
            current = current.nxt()
        return f'{data_all}'


