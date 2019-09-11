def eat(n):
    if n is 1:
        print('eat',n,end = ' ')
    else:
        eat(n-1)
        print('eat',n,end = ' ')
        

eat(5)