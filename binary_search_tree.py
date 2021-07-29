class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def get_leftmost(self):
        curr_node = self
        parent = None
        while curr_node.left:
            parent = curr_node
            curr_node = curr_node.left
        return curr_node, parent


class BST:
    """
    Functions: insert, delete, search
    """
    def __init__(self, data=None):
        if data:
            self.root = Node(data)
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def insert(self, data):
        """
        inserts data into BST
        Note: Duplicate of data cannot be put
        :param data:
        :return: None
        """
        if not self.root:
            self.root = Node(data)
        else:
            curr_node = self.root
            # loop condition
            while True:
                if data == curr_node.data:
                    print("Duplicate! Data already present in tree")
                    break
                elif data > curr_node.data:  # go right
                    if curr_node.right:
                        curr_node = curr_node.right
                    else:
                        # attach to leaf
                        curr_node.right = Node(data)
                        break
                else:  # go left
                    if curr_node.left:
                        curr_node = curr_node.left
                    else:
                        # attach to leaf
                        curr_node.left = Node(data)
                        break
        self.size += 1

    def remove(self, item):
        parent, node = self.lookup_parent(item)
        if node is None:
            raise ValueError("No such item exists")
        if (parent is None) and (node.right is None):
            # root node with no right branch
            self.root = node.left
        else:
            # node with right branch
            self.delete(parent, node)

    @classmethod
    def delete(cls, parent_node, node):
        """
        deletes node from BST
        :param parent_node:
        :param node:
        :return:
        """
        node_right = node.right
        if node_right:
            leftmost_node, parent_leftmost_node = node_right.get_leftmost()
            if parent_leftmost_node is None:  # single child and no right branch
                node.data = node_right.data
                node.right = node_right.right
            else:
                node.data = leftmost_node.data
                BST.delete(parent_leftmost_node, leftmost_node)
        else:
            if node == parent_node.left:
                parent_node.left = node.left
            else:
                parent_node.right = node.left

    def is_empty(self):
        return not self.root

    def lookup(self, data):
        """
        returns node in which data is present
        :param data:
        :return:
        """
        curr_node = self.root
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            elif curr_node.data > data:
                # go left
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None

    def lookup_parent(self, data):
        parent = None
        curr_node = self.root
        while curr_node is not None:
            if curr_node.data == data:
                break
            else:
                parent = curr_node
                if curr_node.data > data:
                    # go left
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
        return parent, curr_node

    def tree_height(self):
        self.calc_depth(self.root)

    @classmethod
    def calc_depth(cls, node):
        if node is None:
            return 0
        else:
            return 1 + max(cls.calc_depth(node.left), cls.calc_depth(node.right))

    @classmethod
    def choose_longer(cls, node1, node2):
        """
        returns the longer node
        if depth of nodes same then returns node2
        :param node1:
        :param node2:
        :return:
        """
        dct = {cls.calc_depth(node1): node1,
               cls.calc_depth(node2): node2}
        # print(dct.keys())
        return dct[max(dct.keys())]

    @classmethod
    def is_leaf(cls, node):
        return (node.right is None) and (node.left is None)

    # def all_data(self, parent, tree):
    #


if __name__ == '__main__':
    test_obj = BST()
    l = [8,9,4,7,3]
    for i in l[:]:
        test_obj.insert(i)
    print(test_obj.size)

    for i in [3,7,4,9,0]:
        print(f"root data: {test_obj.root.data}")
        # print(f"first left:{test_obj.root.left.data}")
        # print(f"first right:{test_obj.root.right.data}")
        print(f"item to del: {i}")
        test_obj.remove(i)
        print('-'*10)
        # print(f"current root data: {test_obj.root.data}")

    # print(test_obj.calc_depth(test_obj.root))
    # test_obj.insert(1)
    # print(test_obj.calc_depth(test_obj.root))
    # test_obj.insert(2)
    # print(test_obj.calc_depth(test_obj.root))
    # test_obj.delete(1)
    # print(test_obj.calc_depth(test_obj.root))
    # test_obj.insert(3)
    # print(test_obj.calc_depth(test_obj.root))
    # # test_obj.insert(-1)
    # # test_obj.insert(-2)
    # # test_obj.insert()
    # print(test_obj.root.left)
    # n = Node()
    # print(test_obj.root.left.data)
    # print(test_obj.choose_longer(test_obj.root.left, test_obj.root).data)





