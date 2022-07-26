"""Árboles binarios"""


class Node:
    """Definición de clase node"""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_inorder(self, node=None):
        """Imprime inorder los items del árbol binario"""
        node = self if not node else node

        if node.left:
            self.print_inorder(node.left)

        print(node.data, end=" ")

        if node.right:
            self.print_inorder(node.right)

    def print_preorder(self, node=None):
        """Imprime preorder los items del árbol binario"""
        node = self if not node else node

        print(node.data, end=" ")

        if node.left:
            self.print_inorder(node.left)

        if node.right:
            self.print_inorder(node.right)

    def print_posorder(self, node=None):
        """Imprime posorder los items del árbol binario"""
        node = self if not node else node

        if node.left:
            self.print_inorder(node.left)

        if node.right:
            self.print_inorder(node.right)

        print(node.data, end=" ")

    def print_levelorder(self):
        """Imprimirá los elementos el árbol en order de nivel"""
        queue = [self]

        while len(queue) > 0:
            print(queue[0].data, end=" ")

            if queue[0].left:
                queue.append(queue[0].left)

            if queue[0].right:
                queue.append(queue[0].right)

            queue.pop(0)

    def insert(self, data):
        """Inserta de manera inorder un elemento dentro del árbol"""
        if not self.data:
            self.data = data
        else:
            queue = [self]

            while len(queue):
                temp = queue[0]
                queue.pop(0)

                if not temp.data:
                    temp.data = data
                    break
                else:
                    if not temp.left:
                        temp.left = Node(data)
                        break
                    else:
                        queue.append(temp.left)

                    if not temp.right:
                        temp.right = Node(data)
                        break
                    else:
                        queue.append(temp.right)

    # def delete_deepest(self, to_delete):
    #     """Permite eliminar un nodo por su ubicación en memoria, de el lado más a la derecha del árbol"""
    #     queue = [self]
    #
    #     while len(queue):
    #         temp = queue.pop(0)
    #         if temp is to_delete:
    #             temp = None
    #             break
    #
    #         if temp.right:
    #             if temp.right is to_delete:
    #                 temp.right = None
    #             else:
    #                 queue.append(temp.right)
    #
    #         if temp.left:
    #             if temp.left is to_delete:
    #                 temp.left = None
    #             else:
    #                 queue.append(temp.left)

    def delete(self, data):
        """Permite eliminar un nodo por su valor"""
        queue = [self]
        to_delete = None
        temp = None
        parent = None

        # Recorremos los nodos del árbol para realizar la búsqueda
        while len(queue):
            temp = queue.pop(0)

            if temp.data == data:
                to_delete = temp

            if temp.left:
                parent = temp
                queue.append(temp.left)

            if temp.right:
                parent = temp
                queue.append(temp.right)

        # Si se ha encontrado el nodo se procederá a reemplazar su valor por el último nodo
        if to_delete:
            print('This parent: ', parent.right.data)
            # Almacenamos el valor del último nodo para intercambiarlo por el nodo a eliminar
            value = temp.data

            # Eliminamos la referencia al último nodo desde el nodo padre
            if parent:
                if parent.left and parent.left.data == value:
                    parent.left = None
                elif parent.right and parent.right.data == value:
                    parent.right = None

            # Intercambiamos el valor
            to_delete.data = value

        return to_delete


if __name__ == '__main__':
    root = Node(13)
    root.left = Node(12)
    root.left.left = Node(4)
    root.left.right = Node(19)
    root.right = Node(10)
    root.right.left = Node(16)
    root.right.right = Node(9)

    # Imprimimos inorder
    print("Inorder:")
    root.print_inorder()
    # Imprimimos en preorder
    print("\nPreorder:")
    root.print_preorder()
    # Imprimimos en posorder
    print("\nPosorder:")
    root.print_posorder()
    # Imprimimos en Level order
    print("\nLevel order:")
    root.print_levelorder()

    print("\nInorder before delete:")
    root.print_inorder()

    root.delete(12)

    print("\nInorder after delete:")
    root.print_inorder()
