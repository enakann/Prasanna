class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


class DLL:
    def __init__(self):
        self.head=None

    def add(self,val):
        if not self.head:
            self.head=Node(val)
        else:
            cur=self.head
            prev=self.head
            while cur.next:
                prev=cur
                cur=cur.next
            cur.next=Node(val)
            cur.prev=prev
    def printl(self):
        cur=self.head
        while cur:
            #print(cur.prev.val)
            print(cur.val)
            if cur.next:
                print("Next is {}".format(cur.next.val))
            cur=cur.next


ll=DLL()
for i in range(3):
    ll.add(i)

ll.printl()