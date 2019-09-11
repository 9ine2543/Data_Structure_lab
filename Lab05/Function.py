def eat(n):
    if n is 1:
        print('eat',n,end = ' ')
    else:
        eat(n-1)
        print('eat',n,end = ' ')
eat(5)
def fac(n):
    if n is not 1:
        n = n * fac(n-1)
    return n
print('',fac(5))

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

def fib(n):
    if n is 2 or n is 1:
        n = 1
    else:
        n = fib(n-1) + fib(n-2)

    return n
print('',fib(4))

def binarySearch(lo,hi,x,l):
    if(hi < lo):
        return None
    m = int((lo+hi)/2)
    if x is l[m]:
        return m
    elif l[m] < x :
        return binarySearch(m+1,hi,x,l)
    else:
        return binarySearch(lo,m-1,x,l)

inp = int(input('Enter your list : '))
l = []
while inp >  0:
    l.append(inp % 10)
    inp  = int(inp / 10)
l.reverse()
print(binarySearch(0,len(l)-1,2,l))