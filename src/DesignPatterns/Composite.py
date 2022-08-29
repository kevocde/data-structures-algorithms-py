from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    def operation(self) -> str:
        return 'Leaf'


class Composite(Component):
    def __init__(self):
        super().__init__()
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())

        return f"Branch({'+'.join(results)})"


if __name__ == '__main__':
    tree = Composite()

    branch = Composite()
    branch.add(Leaf())
    branch.add(Leaf())

    branch_2 = Composite()
    branch_2.add(Leaf())
    branch_2.add(Leaf())
    branch_2.add(Leaf())
    branch_2.add(Leaf())
    branch_2.add(Leaf())

    tree.add(branch)
    tree.add(branch_2)

    print(tree.operation())
