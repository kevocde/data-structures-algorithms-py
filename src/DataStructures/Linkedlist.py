# Clase nodo
class Node:
    # Función para inicializar el nodo
    def __init__(self, data) -> None:
        self.data = data  # La carga útil
        self.next = None  # La referencia al siguiente nodo


class LinkedList:
    """Lista enlazada, esta clase da la definición de la estructura y operaciones"""

    def __init__(self) -> None:
        """Inicialización de clase"""
        self.head = None

    def iterate(self):
        """Devuelve un iterable recorriendo cada uno de los nodos de la lista enlazada"""
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def prepend(self, data):
        """Crea un nuevo nodo en el inicio de la lista enlazada"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        """Crea un nuevo nodo al final de la lista enlazada"""
        if self.head is None:
            self.head = Node(data)
        else:
            nodes = [item for item in self.iterate()]
            nodes[-1].next = Node(data)

    def delete(self, data=None):
        temp = self.head

        if temp is not None and temp.data == data:
            self.head = temp.next
            return
        else:
            prev = None
            while temp is not None:
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next

            if temp is not None:
                prev.next = temp.next


if __name__ == "__main__":
    # Iniciamos la lista
    llist = LinkedList()

    # Creamos y enlazamos los nodos
    llist.append(1)
    llist.append(2)
    llist.append(3)

    # El resultado será
    # |1| ---> |2| ---> |3| ---> None

    llist.prepend(0)
    llist.delete(2)

    # Recorreremos la lista enlazada
    for idx, value in enumerate(llist.iterate()):
        print(f"Node {idx}: {value.data}")
