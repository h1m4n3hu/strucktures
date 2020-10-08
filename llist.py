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


ll=LList()
n1=Node(1)
ll.add(n1)
n2=Node(2)
ll.add(n2)
n3=Node(3)
ll.add(n3)
n3=Node(4)
ll.add(n3)
n4=Node(5)
ll.add(n4)

ll.show()