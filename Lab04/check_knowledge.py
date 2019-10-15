class linkedList:
    class Node:
        def __init__(self,data = None,next = None):
            self.data = data
            self.next = next
            if next is None:
                self.prev = None
            else:
                self.next.prev = self
        def setNext(self,next):
            self.next = next
            self.next.prev = self

    def __init__ (self):
        self.head = self.tail = self.Node()
        self.size = 0
    def __str__(self):
        tmp = self.head.next
        s = ''
        while tmp.next is not None:
            s = s + str(tmp.data) + ' '
            tmp = tmp.next
        s = s + str(tmp.data)
        return s
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def add(self,data):
        if self.isEmpty() :
            self.head.setNext(self.Node(data))
            self.tail = self.head.next
            self.size += 1
        else:
            tmp = self.head.next
            while data >= tmp.data and tmp.next is not None :
                tmp = tmp.next
            if data < tmp.data :
                tmp.prev.setNext(self.Node(data,tmp))
            else:
                tmp.setNext(self.Node(data))
                tmp = tmp.next
                if tmp.next is None:
                    self.tail = tmp
    
l = linkedList()
l.add(5)
l.add(3)
l.add(9)
l.add(7)
l.add(11)
print('List : ',l)

f = 21.91666
#21.92
print("%.2f"%(f))
print("{:.2f}".format(f))

    