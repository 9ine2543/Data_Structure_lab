from Class import node
from Class import myList

d = node('D')
c = node('C',d)
b = node('B',c)
a = node('A',b)

l = myList(a)

print(l)