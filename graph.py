class Graph:
    def __init__(self):
        """
        undirected graph using adjacency list
        """
        self.adjacency_list = {}
        self.count_nodes = 0

    def add_vertex(self, node):
        self.adjacency_list[node] = []
        self.count_nodes += 1

    def add_edge(self, node1, node2):
        """
        undirected
        :param node1:
        :param node2:
        :return:
        """
        if self.adjacency_list.get(node1) is None:
            self.add_vertex(node1)
        if self.adjacency_list.get(node2) is None:
            self.add_vertex(node2)

        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def remove_edge(self, edge):
        pass

    def remove_vertex(self, node):
        pass

    def show_connections(self):
        for i in self.adjacency_list.items():
            print(i[0], '-->', i[1])


if __name__ == "__main__":
    g = Graph()
    g.show_connections()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(0)
    g.show_connections()
    g.add_edge(1,2)
    g.add_edge(1,0)
    g.add_edge(2,0)
    g.show_connections()