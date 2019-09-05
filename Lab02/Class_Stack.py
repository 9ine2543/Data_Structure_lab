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