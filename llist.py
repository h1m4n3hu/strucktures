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

    def remove(self,pos):
        i=0
        first=self.head



ll=LList()
n1=Node(19)
ll.add(n1)
n2=Node(22)
ll.add(n2)
n3=Node(23)
ll.add(n3)
n3=Node(25)
ll.add(n3)
ll.length()

ll.show()