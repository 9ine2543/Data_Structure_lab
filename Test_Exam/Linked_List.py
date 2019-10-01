class singly_list:
    class node:
        def __init__(self, data = None,next = None):
                self.data = data
                if next is None:
                    self.next = None
                    self.prev = None
                else:
                    self.next = next
                    self.next.prev = self
    
    # def __init__(self, head = None): #V.1
    #     if head is None:
    #         self.head = None
    #         self.size = 0
    #     else:
    #         self.head = head 
    #         self.size = 1
    def __init__(self):
        self.head = self.tail = node() #dummy
        self.size = 0
    def addHead(self,data):
        self.head.next = node(data,self.head.next)
        if self.isEmpty():
            self.tail = self.head.next
        self.size += 1 
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def append(self,data):
        if self.isEmpty :
            self.head.next = self.tail = node(data,self.head.next)
            self.size += 1
        else:
            self.tail.next = node(data)
            self.size += 1