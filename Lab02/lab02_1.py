from Stack import Stack

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