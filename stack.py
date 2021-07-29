from linked_list import Node


class StackLinked:
    """
    Implementation1: Using Linked List
    functions to define: push, pop, peek, is_empty
    LIFO, LastInFirstOut
    """
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
            self.size = 1
        else:
            self.head = None
            self.size = 0

    def is_empty(self):
        return not bool(self.head)

    def push(self, data):
        """
        pushes data with a new node onto the stack
        :param data: Any
        :return: None
        """
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.update_link(self.head)
            self.head = new_node
        self.size += 1

    def pop(self):
        """
        removes top or head node
        :return: data in top node
        """
        if self.is_empty():
            raise IndexError("Nothing to pop. Stack is empty")
        else:
            data = self.head.data
            self.head = self.head.nxt()
            self.size -= 1
            return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Nothing to peek. Stack is empty")
        else:
            return self.head.data

    def __repr__(self):
        current = self.head
        data = []
        for i in range(0, self.size):
            data.append(current.data)
            current = current.nxt()
        return f'{data}'


class StackArray:
    """
      Implementation1: Using List
      functions to define: push, pop, peek, is_empty
      LIFO, LastInFirstOut
    """

    def __init__(self, data=None):
        if data:
            self.__list = [data]
            self.size = 1
        else:
            self.__list = []
            self.size = 0

    def is_empty(self):
        return not bool(self.size)

    def push(self, data):
        """
        pushes data with a new node onto the stack
        :param data: Any
        :return: None
        """
        if len(self.__list) > self.size:
            self.__list[self.size] = data
        else:
            self.__list.append(data)
        self.size += 1

    def pop(self):
        """
        removes top or head node
        :return: data in top node
        """
        if self.is_empty():
            raise IndexError("Nothing to pop. Stack is empty")
        else:
            data = self.__list[self.size - 1]
            del self.__list[self.size - 1:]
            self.size -= 1
            return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Nothing to peek. Stack is empty")
        else:
            return self.__list[self.size - 1]

    def __repr__(self):
        return f'{self.__list[::-1]}'


if __name__ == '__main__':
    stack_l = StackLinked()
    stack_a = StackArray()
    print(stack_l, '\n', stack_a)
    # # Test1 peek empty
    # print("Test1 peek empty")
    # print(stack_a.peek())
    # print(stack_l.peek())

    # Test2 push data1
    print('Test2 push data1')
    stack_l.push(1)
    stack_a.push(1)
    print(stack_l, '\n', stack_a)

    # Test3 push data2
    print('Test3 push data2')
    stack_l.push(2)
    stack_a.push(2)
    print(stack_l, '\n', stack_a)

    # Test4 pop data2
    print('Test4 pop data2')
    print(stack_l.pop())
    print(stack_a.pop())
    print(stack_l, '\n', stack_a)

    # Test5 push data2 after pop
    print('Test5 push data2 after pop')
    stack_l.push(3)
    stack_a.push(3)
    print(stack_l, '\n', stack_a)

    # Test6 pop data till empty
    print('Test6 pop data till empty')
    for i in range(0, stack_a.size):
        stack_l.pop()
        stack_a.pop()
    print(stack_l, '\n', stack_a)

    # Test7 is_empty()
    print('Test7 is_empty')
    print(stack_l.is_empty(), '\n', stack_a.is_empty())
    print(stack_l, '\n', stack_a)
