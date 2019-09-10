from Class import List
from Class import node


def bottomUp(l, num):
    count = num / 100.0 * l.size
    for i in range (0,int(count)):
        temp = l.head
        ref = l.head
        while(temp.next):
            temp = temp.next
        temp.next = ref
        l.head = ref.next
        ref.next = None

    return l

def riffle(l,num):
    count = num / 100.0 * l.size

l = List(node(1))
for i in range(2, 11):
    l.append(i)
print(l)
percent = int(input("Enter your percent to bottom up:"))
print(bottomUp(l,percent))


