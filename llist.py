class Node:
    def __init__(self,a):
        self.value=a
        self.next=None

class LList:
    def __init__(self):
        self.head=None

    def show(self):
        first=self.head
        while True:
            if first is not None:
                print(first.value)
                first=first.next
            else:
                break

    def add(self,new):
        if self.head is None:
            self.head=new

        else:
            first=self.head
            while first.next is not None:
                first=first.next
            first.next=new

    def addtop(self,mew):
        first=self.head
        self.head=mew
        mew.next=first

    def pop(self):
        first=self.head
        while first.next is not None:
            prev=first
            first=first.next
        prev.next=None

    def poptop(self):
        first=self.head
        second=self.head.next
        self.head=second
        first.next=None

    def length(self):
        first=self.head
        i=0
        while first is not None:
            first=first.next
            i+=1
        print(i)

    def removeAt(self,pos):
        i=0
        first=self.head
        while first is not None:
            if i==pos:
                prev.next=first.next
                first.next=None
            prev=first
            first=first.next
            i+=1

    def positionOf(self,el):
        first=self.head
        i=0
        while first is not None:
            if first.value==el:
                return i
            first=first.next
            i+=1

    def delete(self,val):
        k=self.positionOf(val)
        self.removeAt(k)

    def sum(self):
        first=self.head
        sum=0
        while first is not None:
            sum+=first.value
            first=first.next
        return sum

    def reverse(self):
        first=self.head
        cur=None
        while first is not None:
            k=first.next
            first.next,cur=cur,first
            #cur=first
            first=k
        self.head=cur

    def even(self):
        first=self.head
        while first is not None:
            if first.value%2==0:
                print(first.value)
            first=first.next

    def isFibb(self):
        first=self.head
        while first and first.next and first.next.next:
            if first.value+first.next.value==first.next.next.value:
                print(first.next.next.value)
            else:
                pass
            first=first.next

    def isPal(self,l1,l2):
        if k1==k2:return True
        else:return False


ll=LList()
ll.add(Node(1))
ll.add(Node(2))
ll.add(Node(3))
ll.add(Node(4))
ll.add(Node(5))
#ll.add(Node(6))
#ll.add(Node(7))
#ll.add(Node(8))
#ll.add(Node(9))
k1=ll
print(k1.head.value)
#k1.show()
print("===")
ll.reverse()
k2=ll
#k2.show()
print(k2.head.value)
print(ll.isPal(k1,k2))

#ll.show()