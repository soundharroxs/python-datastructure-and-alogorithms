
class node :
    def __init__(self,data):
        self.data = data
        self.ref = None


class linked_list:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head == None:
            print("the linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data,"-- >",end = "")
                self.head = self.head.ref

    def enqueue(self,data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def dequeue(self):
        if self.head is None:
            print("the list is empty no node found")
        if self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def is_empty(self):
        if self.head is None:
            print("linked list is empty")
        else:
            print("not empty")
    def peek(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            print(n.data)

l = linked_list()
l.enqueue(23)
l.enqueue(2323)
l.enqueue(3)
l.enqueue(1)
l.dequeue()
l.print_linked_list()

