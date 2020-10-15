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

    def show(self):
        first=self.head
        while first is not None:
            print(first.value)
            first=first.next

    def pair_swap(self):
        k=self.head
        while k and k.next and k.next.next:
            k.value,k.next.value=k.next.value,k.value
            k=k.next.next

    def xs_xl(self):
        k=self.head
        xs=self.head
        xl=self.head
        while k:
            if k.value>xl.value:
                xl=k
            if k.value<xs.value:
                xs=k
            k=k.next
        print(xs.value,xl.value)

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

    def sortlicates(self):
        k=self.head
        while k and k.next:
            if k.value==k.next.value:
                k.next=k.next.next
                continue
                print("hello")
            k=k.next


l=LList()
l.push(Node(11))
l.push(Node(22))
l.push(Node(22))
l.push(Node(33))
l.push(Node(44))
l.push(Node(55))
l.push(Node(55))
l.push(Node(55))
l.push(Node(66))
l.push(Node(77))
l.push(Node(88))
l.sortlicates()

l.show()