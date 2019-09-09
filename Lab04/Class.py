class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
          return self.data
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,data):
        self.data = data
    def setNext(self,next):
        self.next = next

class List:
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def __str__(self):
        temp = self.head
        s = ''
        while(temp.next):
            s = s + temp.data + ' '
            temp = temp.next
        s = s + temp.data
        return s

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while (temp.next):
            temp = temp.next

        temp.next = new_node
        self.size += 1

    def addHead(self,data):
        new_node = node(data,self.head)
        self.head = new_node
        self.size += 1

    def isIn(self,data):
        temp = self.head
        while(temp.data != data and temp.next != None ):
            temp = temp.next
        return temp.data == data 