class Node:
    def __init__(self,*args):
        #print(args)
        self.val,self.st=args
        self.left=None
        self.right=None

    def __repr__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root=None

    def insert(self,*val):
        node=Node(*val)

        if self.root is None:
            self.root=node
        else:
            if node.val > self.root.val:
                if self.root.left is None:
                    self.root.left=node
                else:
                    self._insert(self.root.left,node)

            elif node.val < self.root.val:
                if self.root.right is None:
                    self.root.right = node
                else:
                    self._insert(self.root.right, node)
            else:
                print(f"Node{node} is already in tree")

    def _insert(self,node,val):
            if val.val > node.val:
                if not node.left:
                    node.left=val
                else:
                    self._insert(node.left,val)
            elif val.val < node.val:
                if not node.right:
                    node.right=val
                else:
                    self._insert(node.right,val)

    def pprint(self,curnode):
        #curnode=self.root
        if curnode:
            print(curnode.val,curnode.st)
        if curnode.left:
            self.pprint(curnode.left)
        if curnode.right:
            self.pprint(curnode.right)





bb=BST()

from random import shuffle

s="this is a string containing various letters"

words=[(i,j) for i,j in enumerate(s.split())]

shuffle(words)
print(words)


for i in words:
    #print(i)
    bb.insert(*i)

bb.pprint(bb.root)