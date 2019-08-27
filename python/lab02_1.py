class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items) - 1]

test = Stack()
name = input("Enter your name : ")
for k in name:
    test.push(k)
    print("size ",test.size())


print(test.items)
while test.items != [] :
    print("pop ",test.pop())

print(test.isEmpty())
name = input("Enter your name (again) : ")
for k in name:
    test.push(k)

print("Last char ",test.peek())
print(test.items)
print("Empty ",test.isEmpty())