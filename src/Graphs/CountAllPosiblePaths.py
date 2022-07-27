"""Este algorimo permite hallar todos los caminos posibles entre dos nodos"""


class Graph:
    def __init__(self, size):
        self.size = size
        self.adj = [[] for _ in range(self.size)]

    def add_edge(self, source, destination):
        self.adj[source].append(destination)

    def count_paths_own(self, source, destination, visited=None, path_count=None):
        """Cuenta la cantidad de rutas entre los nodos source y destination"""
        visited = [False] * self.size if visited is None else visited
        path_count = [0] if path_count is None else path_count

        # Se declara que el nodo de búsqueda ya fué visitado para evitar iteracciones
        visited[source] = True

        if source == destination:
            # Este es el caso base en el cuál si llega a que el origen y el destino son iguales, existe una ruta
            path_count[0] += 1
        else:
            # Iteramos por la lista adyacente del nodo origen
            for i in range(len(self.adj[source])):
                if not visited[self.adj[source][i]]:
                    # En caso de no haber sido visitado, se intercambiará la el nodo origen por su nodo relacionado
                    # en la lista adyacente
                    self.count_paths_own(self.adj[source][i], destination, visited, path_count)

        # Despúes de recorrer la lista de nodos adyacentes al de origen, se debe desmarcar el nodo origen cómo visitado
        # para que en el siguiente ciclo (si lo hay), ese pueda ser marcado cómo una posible ruta
        visited[source] = False

        return path_count[0]


if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(1, 3)

    source_node = 2
    destination_none = 3
    print("The number of paths between [{0}] and [{1}] is:".format(source_node, destination_none), end=" ")
    print(graph.count_paths_own(source_node, destination_none))
