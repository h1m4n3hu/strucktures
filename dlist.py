class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class Dll:
    def __init__(self):
        self.head=None

    def append(self,a):
        if self.head==None:
            self.head=a
            a.prev=None
            a.next=None
        else:
            first=self.head
            while first is not None:
                last=first
                first=first.next
            last.next=a
            a.prev=last
            a.next=None

    def prepend(self,a):
        first=self.head
        if first is None:
            self.head=a
            a.next=None
            a.prev=None
        else:
            a.next=self.head
            a.prev=None
            self.head.prev=a
            self.head=a

    def show(self):
        first=self.head
        while first is not None:
            print(first.value)      #print(first.value,first.next.value,first.prev.value)
            first=first.next      #amazing!! !! !!

l=Dll()
n1=Node(10)
l.append(n1)
n2=Node(20)
l.append(n2)
n3=Node(30)
l.append(n3)
n4=Node(40)
l.append(n4)
n5=Node(50)
l.append(n5)
n6=Node(60)
l.append(n6)


l.show()