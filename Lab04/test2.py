class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = self.tail = self.Node(None)
    def __str__ (self):
        l = []
        p = self.head.next
        while p is not None:
            l.append(p.data)
            p = p.next
        return str(l)
    
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        size = 0
        p = self.head.next
        while p is not None:
            size += 1
            p = p.next
        return size
    def append(self, data):
        newNode = self.Node(data)
        self.tail.next = newNode
        self.tail = newNode
    def before(self, data):
        p = self.head.next
        while p.next is not None:
            if p.next.data == data:
                return p
            else:
                p = p.next
        return self.head
            
    def add(self, data):
        p = self.head.next
        newNode = self.Node(data)
        while p is not None:
            if data <= p.data:
                self.before(p.data).next = newNode
                newNode.next = p
                return 
            p = p.next
        self.append(data)

def mean(l):
    p = l.head.next
    tmp = 0
    while p is not None:
        tmp += p.data
        p = p.next
    return float(tmp/len(l))

def mode(l):
    ll = []
    p = l.head.next
    while p is not None:
        ll.append(p.data)
        p = p.next
    maxCount = max(map(ll.count, ll))
    if maxCount == 1:
        return '"NO mode"'
    else:
        mode = []
        for i in ll:
            if ll.count(i) == maxCount:
                mode.append(i)
        mode = list(set(mode))
        return mode

def median(l):
    ll = []
    count = 0
    p = l.head.next
    while p is not None:
        ll.append(p.data)
        count += 1
        p = p.next
    if count %2 == 1:
        return ll[count//2]
    else:
        return (ll[count//2]+ll[(count//2)-1])/2


l = LinkedList()
l.add(3)
l.add(3)
l.add(9)
l.add(17)
l.add(60)
l.add(72)
l.add(42)
l.add(13)
print(l)

print('mean {0:.2f}'.format(mean(l)))
print('mode',mode(l))
print('mde',median(l))
print('mode',mode(l))