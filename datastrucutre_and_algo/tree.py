import queue

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def __repr__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root=None

    def insert(self,val):
        node=Node(val)

        if self.root is None:
            self.root=node
        else:
            self._insert(self.root,node)

    def _insert(self,node,val):
            if val.val < node.val:
                if not node.left:
                    node.left=val
                else:
                    self._insert(node.left,val)
            elif val.val > node.val:
                if not node.right:
                    node.right=val
                else:
                    self._insert(node.right,val)

    def height(self,node):
        if node is None:
            return -1
        else:
            left=self.height(node.left)
            right=self.height(node.right)
            return max(left,right)+1

    def findmin(self):
        cur=self.root
        if not cur:
            return -1
        while cur.left:
            cur=cur.left
        return cur.val

    def findmax(self):
        cur=self.root
        tot=0

        if not cur:
            return -1
        while cur.right:
            tot+=cur.val
            cur=cur.right
        tot+=cur.val
        print(f"sum is {tot}")
        return cur.val




    def pprint(self,curnode):
        #curnode=self.root
        if curnode:
            print(curnode.val)
        if curnode.left:
            self.pprint(curnode.left)
        if curnode.right:
            self.pprint(curnode.right)

    def bfs(self):

        cur=self.root
        q=queue.Queue()

        q.put(cur)

        while not q.empty():
            node=q.get()
            print(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def dfs(self):
        cur=self.root
        ls=[cur]

        while ls:
            node=ls.pop()
            print(node.val)

            if node.left:
                ls.append(node.left)
            if node.right:
                ls.append(node.right)


    def is_bst(self,node):
        if node.left:
            print(f"left nodes {node.val, node.left.val}")
            if not node.val > node.left.val:
                return False
            self.is_bst(node.left)
        if node.right:
            print(f"right nodes {node.val, node.right.val}")
            if not node.val < node.right.val:
                return False
            self.is_bst(node.right)
        return True






    def dfs_max(self):
        ls=[]
        cur=self.root
        ls.append(cur)
        results=[]
        sum=0

        while ls:
            node=ls.pop()
            if node.left:
                ls.append(node.left)
                sum+=node.left.val
            else:
                results.append(sum+node.val)
            if node.right:
                ls.append(node.right)
                sum+=node.right.val
            else:
                results.append(sum+node.val)
        print(results)










bb=BST()

bb.insert(21)
bb.insert(13)
bb.insert(30)
bb.insert(10)
bb.insert(18)
bb.insert(25)
bb.insert(35)
bb.pprint(bb.root)

print(bb.height(bb.root))
print(bb.findmin())
print(bb.findmax())

print("Depth first search")

bb.dfs()

print("breadth first search")
bb.bfs()

print("depth first search")
bb.dfs()

print("check bst")

print(bb.is_bst(bb.root))