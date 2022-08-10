"""Ejemplos de estructura de árbol de búsqueda binaria"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value, node=None):
        """Permite insertar un nuevo valor al árbol a la estructura"""
        node = self if not node else node

        if node.data < value:
            node.right = Node(value) if not node.right else self.insert(value, node.right)
        elif node.data > value:
            node.left = Node(value) if not node.left else self.insert(value, node.left)
        else:
            node = Node(value)

        return node

    def get_min_node(self, node=None):
        node = self if not node else node
        current = node
        while current.left:
            current = current.left

        return current

    def delete(self, value, node=None):
        """Permite eliminar un nodo y reeordenar la estructura"""
        node = self if not node else node

        # Buscamos desde izquierda a derecha
        if value < node.data and node.left:
            node.left = self.delete(value, node.left)
            return node
        elif value > node.data and node.right:
            node.right = self.delete(value, node.right)
            return node

        # Intercambiamos el nodo en caso de que su hijo sea nulo
        if not node.left and node.right:
            return None
        elif not node.left:
            temp = node.right
            return temp
        elif not node.right:
            temp = node.left
            return temp

        succ_parent = node
        succ = node.right

        while succ.left:
            succ_parent = succ
            succ = succ.left

        if succ_parent is not node:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right

        node.data = succ.data

        return node

    def search(self, value, node=None):
        """Permite identificar si existe un valor dentro del árbol binario de búsqueda"""
        node = self if not node else node

        if node.data < value:
            return False if not node.right else self.search(value, node.right)
        elif node.data > value:
            return False if not node.left else self.search(value, node.left)
        else:
            return True

    def inorder(self, node=None):
        """Imprime en pantalla todos los nodos inorder"""
        node = self if not node else node

        if node.left:
            self.inorder(node.left)

        print(node.data, end=" ")

        if node.right:
            self.inorder(node.right)


if __name__ == "__main__":
    # Creamos y agregamos elementos al árbol
    root = Node(44)
    root.insert(17)
    root.insert(32)
    root.insert(28)
    root.insert(29)
    root.insert(88)
    root.insert(65)
    root.insert(97)
    root.insert(54)
    root.insert(82)
    root.insert(76)
    root.insert(80)
    root.insert(78)

    # Mostraremos el árbol creado
    print("BST Show: ")
    root.inorder()

    # Buscamos un elemento
    print("\nBST Search:", root.search(20))

    # Eliminaremos un elemento
    print("\nBST Before Delete element 32: ")
    root.inorder()

    root.delete(32)

    print("\nBST After Delete: ")
    root.inorder()

