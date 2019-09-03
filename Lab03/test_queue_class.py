from Class_Queue import Queue
name = input()
test = Queue()
print('Empty : ',test.isEmpty())
for i in name:
    test.enQueue(i)
    print(test.size(),' ',test.items)

print(test.items)
print('Empty : ',test.isEmpty())
test.deQueue()
print(test.items)