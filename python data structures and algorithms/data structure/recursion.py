class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def show(self):
        return self.items

    def empty(self):
        return self.items == []

s = stack()
s.push("1")
s.push("2")
print(s.show())