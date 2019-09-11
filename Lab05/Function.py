def eat(n):
    if n is 1:
        print('eat',n,end = ' ')
    else:
        eat(n-1)
        print('eat',n,end = ' ')
        

eat(5)
print('')
def fac(n):
    if n is not 1:
        n = n * fac(n-1)
    return n
print(fac(5))

def sum1Ton(n):
    if n is not 1:
        n= n + sum1Ton(n-1)
    return n
print(sum1Ton(5))

def printNto1(n):
    if n is not 1:
        print(n,end = ' ')
        n = printNto1(n-1)
    return n
print(printNto1(5))

def print1ToN(n):
    if n is 1:
        print(n,end = ' ')
    else:
        print1ToN(n-1)
        print(n,end = ' ')
    
print1ToN(5)