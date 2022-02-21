class queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def show(self):
        print(self.items)

    def empty(self):
        return self.items == []

q = queue()
q.enqueue(3)
q.enqueue(23)
q.dequeue()
q.show()

