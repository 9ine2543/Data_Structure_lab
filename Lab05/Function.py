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
