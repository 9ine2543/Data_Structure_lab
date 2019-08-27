class Stack:
	def __init__(self, list = None):
		if list == None:
			self.items = []
		else:
			self.items = list

	def push(self,i):
		self.items.append(i)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return len(self.items) == 0

	def peek(self):
		return self.items[len(self.items) - 1]

name = Stack()
name.push('N')
print(name.items)
print(name.size())
name.push('I')
print(name.items)
print(name.size())
name.push('N')
print(name.items)
print(name.size())
name.push('E')
print(name.items[1])
print(name.size())
print(name.peek())