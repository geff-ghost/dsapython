

num_nodes = 5
edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]

# edges = edges + [(4,5), (3,5)]

# print(edges)



class Graph:
    def __init__(self, num_nodes, edges=[]):
        self.num_nodes = num_nodes
        self.edges = edges
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def addEdge(self, nodes, edges):
        self.num_nodes += nodes
        self.edges = self.edges + edges
        self.data = [[] for _ in range(self.num_nodes)]
        for n1, n2 in self.edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return '\n'.join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


graph = Graph(num_nodes, edges)
graph.addEdge(2, [(4,5), (3,5), (0,6), (1,6), (5,6)])
print(graph)