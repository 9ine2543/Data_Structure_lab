class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
