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

myStr = str(input("Equation ==> "))
open_list = ['{','[','(']
close_list = ['}',']',')']
check = Stack()
isPrint = 0
for i in myStr:
	if i in open_list:
		check.push(i)
	elif i in close_list:
		temp = close_list.index(i)
		if(check.size() > 0 and open_list[temp] == check.peek()):
			check.pop()
		

if(check.size() == 0 ):
	print('MATCH')
elif(check.size() != 0 ):
	print('MISMATCH')