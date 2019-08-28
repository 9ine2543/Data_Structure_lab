class StackParking:
	
	def __init__(self, list = None):
		if list == None:
			self.items = []
			self.numCar = 0
			self.spaceLeft = 4
		else:
			self.items = list
			self.numCar = len(list)
			self.spaceLeft = 4 - self.numCar

	def arrive(self,i):
		
		if (self.numCar < 4):
			self.items.append(i)
			self.numCar += 1
			self.spaceLeft -= 1
		else:
			print(i , ' Soi FULL')

	def depart(self,i):
		
		if i in self.items:
			self.numCar -= 1
			self.spaceLeft += 1
			self.temp = []
			j = len(self.items) - 1
			while self.items[j] != i:
				self.temp.append(self.items.pop())
				j -= 1

			self.items.pop()
			while self.temp != []:
				self.items.append(self.temp.pop())
				

		elif self.items == []:
			print('soi empty')

		else :
			print('No ' + i)


	def size(self):
		return len(self.items)

	def isEmpty(self):
		return len(self.items) == 0

	def isFull(self):
		return len(self.items) == 4

	def peek(self):
		return self.items[len(self.items) - 1]

test = StackParking()
test.depart('Car6')
test.arrive('Car1')
test.arrive('Car2')
test.arrive('Car3')
test.arrive('Car4')
test.arrive('Car5')
print("size ",test.size())
print("space left ",test.spaceLeft)
print("soi ",test.items)
test.depart('Car2')
test.depart('Car7')
print("size ",test.size())
print("space left ",test.spaceLeft)
print(test.items)



