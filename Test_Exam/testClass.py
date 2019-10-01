from StackClass import stack
from Queue import queue

num = input('Enter your number : ').split()
l = queue()
for i in num:
    l.enQueue(int(i))

print(l.mirror())