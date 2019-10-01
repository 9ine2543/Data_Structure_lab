from StackClass import stack
class queue:
    def __init__(self, List = None):
        if List is None:
            self.items = []
        else:
            self.items = List
    
    def enQueue(self,item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def mirror(self):
        s = stack()
        for i in range(self.size()):
            t = self.deQueue()
            self.enQueue(t)
            s.push(t)
        while not s.isEmpty():
            self.enQueue(s.pop())
        return self.items