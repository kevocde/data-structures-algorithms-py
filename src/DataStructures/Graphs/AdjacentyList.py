"""Una matriz adyacente permite representar un grafo ponderado (sin pesos) por medio de un arreglo de listas enlazadas"""


class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.graph = [None] * self.vertexes

    def add_edge(self, src, dest):
        """Añade a la lista la relación entre el nodo objetivo y el nodo destino y viceversa"""
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Añadir esto si el grafo es no directo
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertexes):
            print("Adjacenty list of vertex {}\n head".format(i), end="")

            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    vertexes = 5
    graph = Graph(vertexes)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
