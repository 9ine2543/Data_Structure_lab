class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class List:
    def __init__(self, head=None):
        self.head = head
        if head is None:
            self.size = 0
        else:
            self.size = 1

    def __str__(self):
        temp = self.head
        s = ''
        while(temp.next):
            s = s + str(temp.data) + ' '
            temp = temp.next
        s = s + str(temp.data)
        return s

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.size += 1
            self.head = new_node
            return

        temp = self.head
        while (temp.next):
            temp = temp.next

        temp.next = new_node

        self.size += 1

    def addHead(self, data):
        new_node = node(data, self.head)
        self.head = new_node
        self.size += 1

    def isIn(self, data):
        temp = self.head
        while(temp.data != data and temp.next != None):
            temp = temp.next
        return temp.data == data

    def before(self, data):
        temp = self.head
        n = 0
        while(temp.data != data and temp.next != None):
            temp = temp.next
            n += 1
        temp = self.head
        for i in range(n-1):
            temp = temp.next

        return temp

    def remove(self, data):
        if(self.isIn(data)):
            temp = self.head
            if(temp.data == data):
                self.head = temp.next
                remov = temp
                temp = None
            else:
                while (temp.next):
                    if (temp.data == data):
                        remov = temp
                        break
                    prev = temp
                    temp = temp.next

                prev.next = temp.next
                self.size -= 1
            return remov.data
        else:
            return str(data) + ' is not in List'

    def removeTail(self):
        if(self.isEmpty()):
            return 'This list is empty.'
        else:
            temp = self.head
            while(temp.next):
                prev = temp
                temp = temp.next
            prev.next = None
            self.size -= 1
            return temp
            

    def removeHead(self):
        if(self.isEmpty()):
            return 'This list is empty.'
        else:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            return temp
