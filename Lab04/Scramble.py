from Class import List
from Class import node


def bottomUp(l, num):
    count = num / 100.0 * l.size
    for i in range (0,int(count)):
        l.append(l.removeHead().data)

    return l

def riffle(l,num):
    count = num / 100.0 * l.size
    count2 = l.size - count
    temp = l.head
    temp2 = l.head
    for i in range(0,int(count)):
        temp2 = temp2.next
    if(count >= count2):
        l.before(temp2.data).next = None
        for i in range (0,int(count2)):
            nexttemp = temp.next
            nexttemp2 = temp2.next
            temp.next = temp2
            temp2.next = nexttemp
            temp = nexttemp
            temp2 = nexttemp2

    elif(count < count2):
        for i in range (0,int(count)):
            if (i != int(count) - 1):
                nexttemp = temp.next
                nexttemp2 = temp2.next
                temp.next = temp2
                temp2.next = nexttemp
                temp = nexttemp
                temp2 = nexttemp2
            elif (i == int(count)-1):
                temp.next = temp2
    return l

# def deriffle(l,num):


l = List(node(1))
for i in range(2, 11):
    l.append(i)
print(l)
percent = int(input("Enter your percent to bottom up : "))
print(bottomUp(l,percent)) 
rif = int (input("Enter your percent to riffle : "))
print(riffle(l,rif))
#print(deriffle(l,rif))


