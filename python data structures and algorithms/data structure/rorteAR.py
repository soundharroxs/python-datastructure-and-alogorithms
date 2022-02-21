class node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublell:
    def __init__(self):
        self.head = None

    def print_f(self):
        if self.head is None:
            print("empty dll")
        else:
            n =self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.nref

    def print_b(self):
        if self.head is None:
            print("empty dll")
        else:
            n =self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("node is node empty")

    def begin_insert(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:

            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def end_insert(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_data_a(self,data,x):
        if self.head is None:
            print("empty dll")
        else:
            n = self.head
            while n is not None:
                if n.data == x :
                    break
                n = n.nref
            if n is None:
                print("no data in dll")
            else:
                new_node = node(data)
                new_node.nref = n.nref
                n.nref = new_node
                if n.nref is not None:
                    n.nref.pref = new_node
                new_node.pref = n

    def before_add(self,data,x):
        if self.head is None:
            print("empty dll")
        else:
            n = self.head
            while n is not None:
                if n.data == x :
                    break
                n = n.nref
            if n is  None:
                print("no data found")
            else:
                new_node = node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("empty dll")
            return
        if self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.pref = None



    def delete_end(self):
        if self.head is None:
            print("empty dll")
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            # n.nref.pref = None
            n.pref.nref =None

    def delete_value(self,x):
        if self.head is None:
            print("dll eempty")
            return
        if self.head.nref is None and self.head.data == x:
            self.head = None
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n= n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("dll dta not found")














dll = doublell()
# dll.insert_empty(4)
# dll.insert_empty(4)
dll.begin_insert(2)
dll.begin_insert(22)
dll.begin_insert(211)
dll.end_insert(8)
dll.end_insert(1)
# dll.begin_insert(21)
# dll.add_data_a(32,8)
# dll.before_add(322,32)
# dll.before_add(123,21)
dll.delete_value(1)
# dll.delete_begin()
dll.print_f()