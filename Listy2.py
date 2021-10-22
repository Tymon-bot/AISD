from typing import Any


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    value: Any
    next: 'Node'


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, value: Any) -> None:
        value.next = self.head
        self.head = Node

    head: Node
    tail: Node


list_ = LinkedList()
assert list_.head is None
list_.head = Node(1)
second_Node: Node = Node(2)
third_Node = Node(3)
list_.head.next = second_Node
second_Node.next = third_Node


list_.push(Node(1))
list_.push(Node(0))

assert str(list_) == '0 -> 1'
