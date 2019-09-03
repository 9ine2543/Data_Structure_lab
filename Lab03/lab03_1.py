def String2Int(n):
    return ord(n) - 48

def En_or_De(mode,mess,code):
    
    if(mode == 'd' or mode == 'D'):
        finalstr = []
        k = 0
        for i in test:
            for j in i :
                t = ord(j)-String2Int(code[k])
                if(t>122):
                    t = t-123+97
                elif(t>90 and t < 97):
                    t = t-91+65
                k += 1
                finalstr.append(chr(t))
            finalstr.append(' ')

    elif(mode == 'e' or mode == 'E'):
        finalstr = []
        k = 0
        for i in test:
            for j in i :
                
                t = ord(j)+String2Int(code[k])
                if(t>122):
                    t = t-123+97
                elif(t>90 and t < 97):
                    t = t-91+65
                k += 1
                finalstr.append(chr(t))
            if(i != test[len(test)-1]):
                finalstr.append(' ')

    return finalstr

test = input('Enter you text : ').split(' ')
c = input('Enter you code: ').split(' ')
mode = input('Encode(E) or Decode(D): ')
code = []
j = 0
for i in range(len(test)) :
    j += len(test[i])
k = 0 
n = 0
while k < j:
    code.append(c[n])
    k += 1
    n += 1
    if (n == len(c)):
        n = 0
print(En_or_De(mode,test,code))