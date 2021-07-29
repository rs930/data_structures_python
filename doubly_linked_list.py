class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.nxt = None

    def update_next(self, next_node):
        # update reference nxt
        pass

    def update_prev(self, prev_node):
        pass


class DoublyLinkedList:
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
            self.tail = self.head
            self.size = 1
        else:
            self.head = None
            self.tail = self.head
            self.size = 0

    def _first_node(self, node):
        self.head = node
        self.tail = node
        self.size += 1

    def append(self, data):
        new_node = Node(data)
        if self.size:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
        else:
            self._first_node(new_node)

    def prepend(self, data):
        new_node = Node(data)
        if self.size:
            new_node.nxt = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
        else:
            self._first_node(new_node)

    def get(self, index):
        """
        Returns node at index position
        :param index: integer
        :return:
        """
        # check valid index
        self._valid_index(index)
        if index >= 0:
            current = self.head
            for i in range(0, index):
                current = current.nxt
        else:
            current = self.tail
            for i in range(-1, index, -1):
                current = current.prev
        return current

    def _valid_index(self, index):
        if index >= self.size or index < -self.size:
            raise IndexError("Invalid Index")

    def insert(self, index, value):
        self._valid_index(index)
        idx = self._abs_idx(index)
        if idx == 0:
            self.prepend(value)
        elif idx == (self.size - 1):
            self.append(value)
        else:
            prev = self.get(idx-1)
            nxt = prev.nxt
            curr = Node(value)
            prev.nxt = curr
            curr.prev = prev
            curr.nxt = nxt
            nxt.prev = curr
            self.size += 1

    def _abs_idx(self, index):
        if index < 0:
            return self.size + index
        else:
            return index

    def pop_head(self):
        self.head = self.head.nxt
        self.head.prev = None
        self.size -= 1

    def pop_tail(self):
        self.tail = self.tail.prev
        self.tail.nxt = None
        self.size -= 1

    def delete(self, index):
        """
        deletes node at given index
        :param index: integer
        :return: None
        """
        curr_node = self.get(index)
        if self.size == 1:
            self.tail = None

        if self.head == curr_node:
            self.pop_head()

        elif self.tail == curr_node:
            self.pop_tail()

        else:
            prev_node = curr_node.prev
            nxt_node = curr_node.nxt
            prev_node.nxt = nxt_node
            nxt_node.prev = prev_node
            self.size -= 1

    def __repr__(self):
        data_all = []
        current = self.head
        for i in range(0, self.size):
            data_all.append(current.data)
            current = current.nxt
        return f'{data_all}'


if __name__ == '__main__':
    # Test1 __init__
    test = DoublyLinkedList(10)
    test_empty = DoublyLinkedList()
    print('Test1: New LinkedList: {}'.format(test))

    # Test2 isempty
    # print('Test2: Check isempty: {}'.format(test.is_empty()))

    # Test3 append
    test.append(1)
    print('Test3: Check append: {}'.format(test))

    # Test4 get
    print('Test4: Check get: {}'.format(test.get(0).data))
    # note negative numbers give element at head back

    # Test5
    # print('Test5: Check get_node {}'.format(test.get_node(0).data))
    # print('Test5: Check get_node in empty {}'.format(test_empty.get_node().data))

    # Test6
    test.append(2)
    test.append(3)
    test.insert(2, 7)
    print('Test6: Check insert at position2 {}'.format(test))

    # Test7
    # test_empty.insert(0, 0)
    # print('Test7: Check insert in emptylist should give error{}'.format(test_empty))

    # Test8
    test.delete(3)
    print('Test8: Check delete in test {}'.format(test))

    # Test9
    # test_empty.delete(0)
    # print('Test8: Check delete in test_empty {}'.format(test_empty))

    # Test9
    # test.tail()
    print('Test9: Check tail in test: {}'.format(test.tail.data))

    # Test10
    print('Test10: Check tail in test_empty: {}'.format(test_empty.tail.data))
