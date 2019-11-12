class node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self,left):
        self.left = left
        self.left.fp = self

    def setRight(self,right):
        self.right = right
        self.right.fp = self

class BST:
    def __init__(self):
        self.root = None

    def addI(self,data):
        if self.root is None:
            self.root = node(data)
            
        else:
            fp = None
            p = self.root
            while p :
                fp = p
                p = p.left if data < p.data else p.right

            if data < fp.data:
                fp.setLeft(node(data))
            else:
                fp.setRight(node(data))

    def add(self,data):
        self.root = BST._add(self.root,data)

    def _add(root,data):
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.setLeft(BST._add(root,data))
            else:
                root.setRight(BST._add(root,data))
    
    def inOrder(self):
        BST._inOrder(self.root)
        print()
    
    def _inOrder(root):
        if root:
            BST._inOrder(root.getLeft())
            print(root.data, end = ' ')
            BST._inOrder(root.getRight())

    def preOrder(self):
        BST._preOrder(self.root)
        print()
    
    def _preOrder(root):
        if root:
            print(root.data, end = ' ')
            BST._preOrder(root.getLeft())
            BST._preOrder(root.getRight())

    def postOrder(self):
        BST._postOrder(self.root)
        print()
    
    def _postOrder(root):
        if root:
            BST._postOrder(root.getLeft())
            BST._postOrder(root.getRight())
            print(root.data, end = ' ')
        
    def printSideway(self):
        BST._printSideway(self.root,0)
        print()

    def _printSideway(root,level):
        if root:
            BST._printSideway(root.getRight(),level + 1)
            print('\t'*level,root.getData(),sep = '')
            BST._printSideway(root.getLeft(),level + 1)

    def search(self,data):
        return BST._search(self.root,data)

    def _search(root,data):
        if root is None:
            return None
        else:
            if data < root.data:
                return BST._search(root.getLeft(),data)
            elif data > root.data:
                return BST._search(root.getRight(),data)
            elif data == root.data:
                return root

    def path(self,data):
        BST._path(self.root,data)

    def _path(root,data):
        if BST._search(root,data) is None:
             print('None')
        else:
            if data < root.data:
                print(root.data,end = '->')
                BST._path(root.getLeft(),data)
            elif data > root.data:
                print(root.data,end = '->')
                BST._path(root.getRight(),data)
            elif data == root.data:
                print(root.data)
    
    def delete(self,data):
        if BST._search(self.root,data) is None:
            return None
        else:
            if BST._search(self.root,data).right is None and BST._search(self.root,data).left is None:
                tm = BST._search(self.root,data)
                if tm.fp.left == tm:
                    tm.fp.left = None
                else:
                    tm.fp.right = None
            elif BST._search(self.root,data).right is None and BST._search(self.root,data).left is not None:
                tm = BST._search(self.root,data)
                tm.fp.right = tm.left
            
            else:
                temp = BST._search(self.root,data)
                t = BST._delete(temp.getRight())
                temp.setData(t.left.data)
                if t.left.right is None:
                    t.left = None
                    return
                else:
                    t.left = t.left.right
                    return


    def _delete(root,fp = None,gp = None):
        if root is None:
            return gp
        else:
            gp = fp
            fp = root
            return BST._delete(root.getLeft(),fp,gp)

        
            



# l = [int(e) for e in input("insert integers : ").split(' ')]
l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print(l)

t = BST()
for i in l:
    t.addI(i)
# t.inOrder()
t.printSideway()
t.delete(4)
t.printSideway()