from Class import node
from Class import List

a = node('A')
l = List(a)
l.append('B')
l.append('C')
l.addHead('0')

print(l)

print(l.remove('0'),' ',l )
print (l.removeHead(),' ',l)
