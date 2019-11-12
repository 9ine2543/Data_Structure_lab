class node:
		def __init__(self, data = None, next = None):
			self.data = data;
			if next is None:
				self.next = None
				self.prev = None
			else:
				self.next = next
				self.next.prev = self


class LinkedList:

	def __init__(self, head = None): #V.1
		if head is None:
			self.head = self.tail = node()
			self.size = 0
		else:
			self.head = head 
			self.size = 1
	def __str__(self):
		temp = self.head.next #frist node
		s = ''
		while temp.next is not None:
			s = s + str(temp.data) + ' '
			temp = temp.next
		return s

	def addHead(self,data):
		self.head.next = node(data,self.head.next)
		if self.isEmpty():
			self.tail = self.head.next
		self.size += 1 

	def getSize(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def append(self,data):
		if self.isEmpty :
			self.head.next = self.tail = node(data,self.head.next)
			self.size += 1
		else:
			self.tail.next = node(data)
			self.size += 1

	def nodeAt(self,index):
		temp = self.head.next
		for i in range(index):
			temp = temp.next
		return temp

test = LinkedList()
test.addHead(0)
print(test)
test.append(1)
print(test)
test.append(2)
print(test)
test.append(3)
print(test)
test.append(4)
print(test)
