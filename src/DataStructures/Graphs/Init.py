"""Ejemplos y algoritmos con la estructura de datos tipo grafo"""


class Graph:
    def __init__(self, num_vertexes):
        self.num_vertexes = num_vertexes
        self.adj_matrix = [[-1] * num_vertexes for x in range(num_vertexes)]
        self.vertexes = {}
        self.vertexes_list = [0] * num_vertexes

    def set_vertex(self, vertex, value):
        if 0 <= vertex <= self.num_vertexes:
            self.vertexes[value] = vertex
            self.vertexes_list[vertex] = value

    def set_edge(self, frm, to, weight):
        frm = self.vertexes[frm]
        to = self.vertexes[to]
        self.adj_matrix[frm][to] = weight

        # Solo para grafos que no son directos
        self.adj_matrix[frm][to] = weight

    def get_vertexes(self):
        return self.vertexes_list

    def get_edges(self):
        edges = []
        for i in range(self.num_vertexes):
            for j in range(self.num_vertexes):
                if self.adj_matrix[i][j] != -1:
                    edges.append((self.vertexes_list[i], self.vertexes_list[j], self.adj_matrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adj_matrix


graph = Graph(6)
graph.set_vertex(0, 'a')
graph.set_vertex(1, 'b')
graph.set_vertex(2, 'c')
graph.set_vertex(3, 'd')
graph.set_vertex(4, 'e')
graph.set_vertex(5, 'f')

# Añadimos las conexiones (arcos)
graph.set_edge('a', 'e', 10)
graph.set_edge('a', 'c', 20)
graph.set_edge('c', 'b', 30)
graph.set_edge('b', 'e', 40)
graph.set_edge('e', 'd', 50)
graph.set_edge('f', 'e', 60)

print("Vertices of graph")
print(graph.get_vertexes())

print("Edges of graph")
print(graph.get_edges())

print("Adjacenty Matrix of graph")
print(graph.get_matrix())