from Class import List, node

def bottomUp(l, num):
    count = num / 100.0 * l.getSize()
    temp = l.head
    while temp.next is not None:
        temp = temp.next
    temp.next = l.head
    while (count != 0):
        temp = temp.next
        count -= 1
    l.head = temp.next
    temp.next = None
    return l


def riffle(l, num):
    count = num / 100.0 * l.size

    # count2 = l.size - count
    # temp = l.head
    # temp2 = l.head
    # for i in range(0,int(count)):
    #     temp2 = temp2.next
    # if(count >= count2):
    #     l.before(temp2.data).next = None
    #     for i in range (0,int(count2)):
    #         nexttemp = temp.next
    #         nexttemp2 = temp2.next
    #         temp.next = temp2
    #         temp2.next = nexttemp
    #         temp = nexttemp
    #         temp2 = nexttemp2

    # elif(count < count2):
    #     for i in range (0,int(count)):
    #         if (i != int(count) - 1):
    #             nexttemp = temp.next
    #             nexttemp2 = temp2.next
    #             temp.next = temp2
    #             temp2.next = nexttemp
    #             temp = nexttemp
    #             temp2 = nexttemp2
    #         elif (i == int(count)-1):
    #             temp.next = temp2
    return l

# def deriffle(l,num):


def debottomUp(l, num):
    count = l.getSize() - (num / 100.0 * l.getSize())
    temp = l.head
    while temp.next is not None:
        temp = temp.next
    temp.next = l.head
    while (count != 0):
        temp = temp.next
        count -= 1
    l.head = temp.next
    temp.next = None
    return l

l = List(node(1))
for i in range(2, 11):
    l.append(i)
print(l)
percent = int(input("Enter your percent to bottom up : "))
print(bottomUp(l, percent))
# rif = int(input("Enter your percent to riffle : "))
# print(riffle(l, rif))
print(debottomUp(l,percent))
# print(deriffle(l,rif))
