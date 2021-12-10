from typing import Any, Callable
import collections


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)
        visit(self)

    def traverse_pre_order(self, visit):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root):
        self.root = BinaryNode(root)

    def traverse_in_order(self, visit):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit):
        self.root.traverse_pre_order(visit)


#Schemat działania funkcji right_line:
# funkcja działa poziomami, przepychając węzły występujące najbardziej z prawej (zgodnie z poleceniem zadania)
# na lewą stronę kolejki, skąd są pobierane przy użyciu appenda i następnie są przekazywane do zmiennej najb, skąd są
# wykorzystywane do analizy następnego poziomu
# całe drzewo jest analizowane poprzez kolejkę deque
# ostatecznie zostaje element, który może nie być prawym dzieckiem korzenia (lub jednym z jego prawych potomków) ale który spełnia
# warunki zadania

def right_line(tree):  # przy użyciu FIFO
    List = []
    q = collections.deque()
    q.append(tree.root)  # zaczynam od korzenia, ponieważ zawsze jest "widoczny" z prawej strony
    while len(q) > 0:   #w czasie, gdy kolejka nie jest pusta:
        size = len(q)
        temp = 0
        List.append(q[0].value)  #zawsze dodaję wartość, stojącą najbardziej po lewej stronie
        while temp < size:

            najb = q.popleft()
            print(najb)
            print(List)
            if najb.right_child is not None:
                q.append(najb.right_child)
            print(najb.right_child)

            if najb.left_child is not None:  # jeżeli zamieniłbym warunki kolejnością to otrzymałbym funkcję left_line
                q.append(najb.left_child)
            print(najb.left_child)

            temp += 1


    return List
#

# # Testy do LAB 5
#
# tree = BinaryTree(10)
# tree.root.add_right_child(2)
# tree.root.right_child.add_left_child(20)
# tree.root.add_left_child(3)
# tree.root.left_child.add_right_child(5)
# tree.root.left_child.add_left_child(1)
#
# assert tree.root.value == 10
#
# assert tree.root.right_child.value == 2
# assert tree.root.right_child.is_leaf() is False
#
# assert tree.root.left_child.left_child.value == 1
# assert tree.root.left_child.left_child.is_leaf() is True

# Testy do projektu

tree = BinaryTree(1)
tree.root.add_right_child(3)
tree.root.right_child.add_right_child(7)
tree.root.add_left_child(2)
tree.root.left_child.add_right_child(5)
tree.root.left_child.add_left_child(4)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)

print(right_line(tree))
