class stack:
    def __init__(self, List = None):
        if List is None:
            self.items = []
        else:
            self.items = List

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return None if self.isEmpty else self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)