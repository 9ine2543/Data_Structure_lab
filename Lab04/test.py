class stack:
    def __init__(self,data = []):
        if data == []:
            self.data = []
        else:
            self.data = data

    def pop(self):
        return self.data.pop()
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.data[-1]
    def push(self,i):
        self.data.append(i)
    def isEmpty(self):
        return self.data == []
    def __str__(self):
        return str(self.data)
    def __len__(self):
        return len(self.data)

class s:
    def __init__(self,data = []):
        if data == []:
            self.data = []
        else:
            self.data = data
    def peek(self):
        return self.data[-1]
    def pop(self):
        return self.data.pop()
    def push(self,i):
        self.data.append(i)
    def isEmpty(self):
        return self.data == []
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)

def inTopost(infix):
    s = stack()
    result = 0
    nubOperand = 0
    nubOperation = 0

    for i in infix:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            result += i
        elif i == '(':
            s.push(i)
        elif i == ')':
            continue















def checkP(peek,cur):
    pPeek = 0
    pCur = 0
    if peek in ['+', '-']:
        pPeek = 1
    else:
        pPeek = 2
    if cur in ['+', '-']:
        pCur = 1
    else:
        pCur = 2
    return pPeek >= pCur

def inTopost(infix):
    s = stack()
    result = ''
    nubOperation = 0
    nubOperand = 0

    for i in infix:
        if 'a' <= i <= 'z' or 'A' <= i <= 'z':
            result += i
            nubOperand += 1
        else:
            if i == '(':
                s.push(i)
            elif i == ')':
                while not s.isEmpty():
                    if s.peek() == '(':
                        s.pop()
                        break
                    else:
                        result += s.pop()
            elif i in ['+', '-', '*', '/']:
                nubOperation += 1
                if checkP(s.peek(),i):
                    while not s.isEmpty():
                        if s.peek() == '(':
                            break
                        else:
                            result += s.pop()
                s.push(i)
    
    while not s.isEmpty():
        result += s.pop()
    return result,nubOperand,nubOperation


def postToin(postfix):
    s = stack()
    infix = ''
    for i in postfix:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            s.push(i)
        else:
            tmp1 = s.pop()
            tmp2 = s.pop()
            tmp3 = '(' + tmp2 + i + tmp1 + ')'
            s.push(tmp3)
    while not s.isEmpty():
        infix += s.pop()
    return infix


infix = input('ff: ')
a,b,c = inTopost(infix)
print('dfbdfb: ',a)
print(b)
print(c)
# postfix = input()

print (postToin(a))

