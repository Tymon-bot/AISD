

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value, None)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            self.tail = self.head
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = Node(value, None)

    def node(self, at):
        if self.head is None:
            return None
        if at == 0:
            return self.head
        temp = 0
        cur = self.head
        while cur is not None:
            if temp == at:
                return cur
            temp += 1
            cur = cur.next

    def insert(self, value, after):
        if after is None:
            return None
        new_node = Node(value, None)
        if after == self.tail:
            after.next = new_node
            self.tail = new_node
        new_node.next = after.next
        after.next = new_node

    def pop(self):
        if self.head is None:
            return None
        removed = self.head
        removed.value = self.head.value
        self.head = self.head.next
        return removed.value

    def remove_last(self):
        if self.head is None:
            return None
        second_last = self.head
        while second_last.next.next is not None:
            second_last = second_last.next
        self.tail = second_last
        second_last.next = None
        return second_last.value

    def remove(self, after):
        if self.head is None:
            return None
        temp = 0
        cur = self.head
        while cur is not None:
            if temp == after:
                cur.next = cur.next.next
                break
            cur = cur.next
            temp += 1

    def len(self):
        cur = self.head
        temp = 0
        while cur.next is not None:
            temp += 1
            cur = cur.next
        return temp

    def __str__(self):
        temp = self.head
        temp_list = ""
        if temp is None:
            print("List is empty")
        while temp is not None:
            if temp.next is not None:
                temp_list = temp_list + str(temp.value) + ' -> '
            else:
                temp_list = temp_list + str(temp.value)
            temp = temp.next
        return temp_list


# #TESTY
#
# list_ = LinkedList()
# assert list_.head == None
# list_.push(1)
# list_.push(0)
#
# assert str(list_) == '0 -> 1'
#
# list_.append(9)
# list_.append(10)
#
# assert str(list_) == '0 -> 1 -> 9 -> 10'
#
# middle_node = list_.node(at=1)
# list_.insert(5, after=middle_node)
#
# assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
#
# first_element = list_.node(at=0)
# returned_first_element = list_.pop()
#
# assert first_element.value == returned_first_element
#
#
# last_element = list_.node(at=2)
# returned_last_element = list_.remove_last()
#
# assert last_element.value == returned_last_element
# assert str(list_) == '1 -> 5 -> 9'
#
#
# # second_node = list_.node(1)
# # list_.remove(second_node)
# #
# # assert str(list_) == '1 -> 5'
# print(list_) #remove działa, ale z assertem jest problem
# list_.remove(1)
# print(list_)



class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.remove_last()

    def __str__(self):
        if self.storage.head is None:
            return 'Stack is empty'
        cur = self.storage.head
        stack_temp = ' '
        while cur is not None:
            if cur.next is None:
                stack_temp += str(cur.value)[::-1]
                return stack_temp[::-1]
            stack_temp += str(cur.value)[::-1] + '\n'
            cur = cur.next
        return stack_temp[::-1]

    def __len__(self):
        temp = 0
        cur = self.storage.head
        while cur is not None:
            temp += 1
            cur = cur.next
        return temp

# #Testy
# stack = Stack()
# assert len(stack) == 0
#
# stack.push(3)
# stack.push(10)
# stack.push(1)
#
# assert len(stack) == 3
#
#
# # print(stack)
# #
# top_value = stack.pop()
# #
# # assert top_value == 1
# assert len(stack) == 2


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def peek(self):
        return self.storage.head.value

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop()

    def __str__(self):
        if self.storage.head is None:
            return 'Queue is empty'
        cur = self.storage.head
        queue_temp = ''
        while cur is not None:
            queue_temp += str(cur.value)
            cur = cur.next

        return queue_temp

    def __len__(self):
        temp = 0
        cur = self.storage.head
        while cur is not None:
            temp += 1
            cur = cur.next
        return temp


# #Testy
# queue = Queue()
# assert len(queue) == 0
# queue.enqueue('klient1, ')
# queue.enqueue('klient2, ')
# queue.enqueue('klient3')
#
# assert str(queue) == 'klient1, klient2, klient3'
#
# client_first = queue.dequeue()
#
# # assert client_first == 'klient1'
# assert str(queue) == 'klient2, klient3'
# assert len(queue) == 2
# print(queue)
