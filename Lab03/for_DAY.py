from Class_Queue import Queue

def EnDe(mode,code,text):
    finaltext = Queue()
    if(mode == 'E' or mode == 'e'):
        
        for i in text:
            if(i != ' '):
                num = ord(i) + code.deQueue()
                finaltext.enQueue(chr(num))
            else:
                finaltext.enQueue(' ')

    elif(mode == 'D' or mode == 'd'):
        
        for i in text:
            if(i != ' '):
                num = ord(i) - code.deQueue()
                finaltext.enQueue(chr(num))
            else:
                finaltext.enQueue(' ')
    return finaltext.items

text_input = input('Enter your text: ')
code_input = input('Enter your code: ')
mode_input = input('Encode(E) or Decode(D): ')
j = 0
n = 0
code = Queue()
for i in text_input:
    if(i != ' '):
        j += 1

for i in range(j):
    code.enQueue(ord(code_input[n])- 48)
    n += 1
    if(n == len(code_input)):
        n = 0


print(code.items)
print(EnDe(mode_input,code,text_input))
