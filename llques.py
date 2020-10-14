class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LList:
    def __init__(self):
        self.head=None

    def push(self,value):
        if self.head==None:
            self.head=value
        else:
            first=self.head
            while first.next is not None:
                first=first.next
            first.next=value

    def place(self,value):
        if self.head==None:
            self.head=value
        else:
            first=self.head
            self.head=value
            value.next=first

    def show(self):
        first=self.head
        while first is not None:
            print(first.value)
            first=first.next

    def length(self):
        i=0
        while self.head:
            self.head=self.head.next
            i+=1
        print(i)

    def ifPresent(self,value):
        while self.head:
            if self.head.value==value:
                return(True)
            self.head=self.head.next

    def setAt(self,index,value):
        i=0
        last=self.head
        while last:
            if i==index:
                last.value=value
            last=last.next
            i+=1

    def del_n_after_m(self,m,n):
        i=0
        j=0
        first=self.head
        while i<m-1:
            first=first.next
            i+=1
        second=first
        while j<n:
            second=second.next
            j+=1
        skip=second.next
        first.next=skip

    def add_1(self):
        first=self.head
        strr=""
        while first:
            strr+=str(first.value)
            first=first.next
        return int(strr)+1

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

    def rotate(self,m):
        i=0
        first=self.head
        while first is not None:
            last=first
            first=first.next
        first=self.head
        while i<m:
            b4=first
            first=first.next
            i+=1
        k=self.head
        self.head=first
        last.next=k
        b4.next=None

l=LList()
l.push(Node(11))
l.push(Node(22))
l.push(Node(33))
l.push(Node(44))
l.push(Node(55))
l.push(Node(66))
l.push(Node(77))
l.rotate(4)

l.show()