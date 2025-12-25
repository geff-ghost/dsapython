
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge_weighted(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print('Adjacency Matrix:')
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print('\nVertex Data:')
        for vertex, data in enumerate(self.vertex_data):
            print(f'Vertex {vertex}: {data}')

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' -> ')

        for i in range(self.size):
            # This is where we check for connections with other nodes
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data) #the index of the start value from the list of vertices
        self.dfs_util(start_vertex, visited)


g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(1, 5)

g.print_graph()

print('\nDepth First Search starting from vertex D:')
g.dfs('D')
