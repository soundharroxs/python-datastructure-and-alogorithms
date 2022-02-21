# class stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self,item):
#         self.items.append(item)
#
#     def pop(self):
#         self.items.pop()
#
#     def show(self):
#         return self.items
#
#     def empty(self):
#         return self.items == []

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

    def add_element(self,data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_begin(self):
        if self.head is None:
            print("the list is empty no node found")
        else:
            self.head = self.head.ref
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
l.add_element(2)
l.add_element(22)
l.add_element(21)
l.delete_begin()
l.peek()

#l.print_linked_list()
"""class payslip:
    def __init__(self,basicsalary,hra,ita):
        self.basicsalary = basicsalary
        self.hra = hra
        self.ita = ita

class payslipdemo:
    def gethighestpf(self,plis):
        high = 0
        for i in plis:
            pf = 0
            pf =  i.basicsalary * 0.12
            if high < pf:
                high = pf

        return high

if __name__ == "__main__":
    count = int(input())
    plist =[]
    for i in range(count):
        basicsalary = int(input())
        hra = int(input())
        ita = int(input())
    plist.append(payslip(basicsalary,hra,ita))
    p = payslipdemo()
    pd = p.gethighestpf(plist)
    print(pd)

"""