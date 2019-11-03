class Node:
    def __init__(self,val):
        self.val=val
        self.next=None



class LL:
    def __init__(self):
        self.head=None


    def add(self,val):
        node=Node(val)
        if self.head is None:
            self.head=node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=node

    def printnode(self):
        cur=self.head
        while cur:
            print(cur.val)
            cur=cur.next

    def reverse(self):
        cur=self.head
        prev=None
        next=None
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        self.head=prev
        self.printnode()
        #self.head=cur

    def delete_nth_from_last(self,n):
        cur1=self.head
        cur2=self.head
        for i in range(n):
            cur1=cur1.next

        while cur1.next:
            cur1=cur1.next
            cur2=cur2.next

        print(cur2.val)





ll=LL()

for i in range(5):
    ll.add(i)

print("Before reversal")
ll.printnode()

print("After reversal")
#ll.reverse()

print("get nth node from end")

ll.delete_nth_from_last(3)