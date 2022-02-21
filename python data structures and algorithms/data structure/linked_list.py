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

    def add_begin(self,data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
               n = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head == None:
             print("the list empty")
             return
        if self.head.data == x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node is not found")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not presnt")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("limked list is not empty")

    def delete_begin(self):
        if self.head is None:
            print("the list is empty no node found")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("the list is empty no node found")
        if self.head.ref is None:
            self.head =None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref =None

    def delete_value(self,x):
        if self.head is None:
            print("the list is empty no node found")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("nod is not present")
        else:
            n.ref = n.ref.ref












l = linked_list()
# l.insert_empty(3)
# l.delete_begin()
# l.add_begin(2)
# l.add_begin(30)
# l.add_begin(45)
l.add_end("2")
l.add_begin("e")
l.add_end("3")
l.add_end("4")
# l.add_before(4,"e")
l.add_before(34,4)
l
# l.delete_value(45)
l.print_linked_list()



