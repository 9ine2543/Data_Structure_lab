class node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right


def inOrder(r):
    if r:
        inOrder(r.left)
        print(r.data,end = '')
        inOrder(r.right)
def add(r,data):
    if not r:
        return node(data)
    else:
        if data < r.data:
            r.left = add(r.left, data)
        else:
            r.right = add(r.right, data)
        return r
def printSideWay(r,level):
    if r:
        printSideWay(r.right,level + 1)
        print(' '*3*level,r.data)
        printSideWay(r.left,level + 1)
def height(r):
    
