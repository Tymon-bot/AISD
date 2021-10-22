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


    head: Node
    tail: Node


    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def append(self, value: Any)-> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while(last_node.next):
            last_node = last_node.next


    # def node(self, at: int)-> Node:









list_ = LinkedList()
# assert list_.head is None
list_.push(1)
list_.push(0)

list_.append(9)
list_.append(10)



# list_.push(Node(1))
# list_.push(Node(0))
# assert str(list_) == '0 -> 1'
# print(len(list_))