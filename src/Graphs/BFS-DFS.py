"""Breadth-First Search Búsqueda por Amplitud y Depth First Search Búsqueda por profundidad"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs(self, src):
        visited = [False] * (max(self.graph) + 1)
        visited[src] = True
        queue = [src]

        while queue:
            src = queue.pop(0)
            print(src, end=" ")

            for i in self.graph[src]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, src, visited=None):
        visited = set() if visited is None else visited

        visited.add(src)
        print(src, end=" ")

        for neighbour in self.graph[src]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")

print("BFS: ", end="")
graph.bfs(2)

print("\nDFS: ", end="")
graph.dfs(2)
