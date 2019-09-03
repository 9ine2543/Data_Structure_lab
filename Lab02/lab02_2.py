from Stack import Stack

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