from Class import node
from Class import List

l = List()
l.addHead('6')
print(l)
print('Empty : ',l.isEmpty())
#print(l.removeTail())
for i in range(1,5):
    l.append(i)
    print(l)
    print('Size : ',l.getSize())

l.remove('6')
print(l,' ',l.getSize())
print(l.before(2).getData())


# l.addHead('0')
# print(l)
# print('Size : ',l.getSize())

# print('Is "1" in List : ', l.isIn(1))
# print('remove head : ', l.removeHead())
# print('remove tail : ', l.removeTail())
# print('remove "2" :' , l.remove(2))
# print('remove "7" :' , l.remove(7))
# print(l)
# print('Size : ',l.getSize())
