def app(n):
    global l
    if n is 1:
        l.append(n)
    else:
        app(n-1)
        l.append(n)

def appB(n):
    global l
    if n is 1:
        l.append(n)
    else:
        l.append(n)
        appB(n-1)
        

l = []
app(10)
appB(10)
print(l)