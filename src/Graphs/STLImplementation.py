"""Implementación simple de un grafo y recorrido del mismo por medio de STL,
este tipo de algoritmos son usados en la programación competitiva"""


class Graph:
    def __init__(self, size):
        self.size = size
        self.adj = [[] for _ in range(self.size)]

    def add_edge(self, src, dest):
        """Añade al arreglo adyacente su relación con el siguiente nodo"""
        self.adj[src].append(dest)
        self.adj[dest].append(src)

    def dfs(self, u=None, adj=None, visited=None):
        """Por medio de el recurrido por profundidad o DFS se recorrerá las matrices adyacentes"""
        visited = [False] * (self.size + 1) if visited is None else visited
        adj = self.adj if adj is None else adj

        if u is None:
            for u in range(self.size):
                if not visited[u]:
                    self.dfs(u, adj, visited)
        else:
            print(u, end=" ")
            visited[u] = True
            for i in range(len(adj[u])):
                if not visited[adj[u][i]]:
                    self.dfs(adj[u][i], adj, visited)


if __name__ == '__main__':
    graph = Graph(5)

    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.dfs()
