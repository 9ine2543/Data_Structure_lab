def String2Int(n):
    return ord(n) - 48

test = input('Enter you text : ').split(' ')
code = input('Enter you code: ').split(' ')
c = ord(test[0][0])+String2Int(code[0])
print(chr(c))