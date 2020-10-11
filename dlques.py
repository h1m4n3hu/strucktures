class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None
class Dlist:
    def __init__(self):
        self.head=None

    def append(self,value):
        if self.head is None:
            self.head=value
            self.prev=None
            self.next=None
        else:
            first=self.head
            while first:
                last=first
                first=first.next
            last.next=value
            value.next=None
            value.prev=last

    def show(self):
        while self.head:
            print(self.head.value)
            self.head=self.head.next

    def showRev(self):
        first=self.head
        while first:
            last=first
            first=first.next
        while last:
            print(last.value)
            last=last.prev

    def rev(self):
        curr = None
        first = self.head
        while first:
            curr=first
            first.next, first.prev = first.prev, first.next
            first = first.prev
        self.head = curr

    def remove(self,index):
        first=self.head
        i=0
        while i<index:
            previ=first
            first=first.next
            nexti=first.next
            i+=1
        previ.next=nexti
        nexti.prev=previ


    def revTedTalks(self):
        curr = None
        first = self.head
        while first:
            curr = first
            "curr = first.prev"
            "first.prev= first.next"
            first.next, first.prev= first.prev, first.next
            "first.next = curr"
            first = first.prev
        self.head=curr


l=Dlist()
l.append(Node(10))
l.append(Node(20))
l.append(Node(30))
l.append(Node(40))
l.append(Node(50))
l.append(Node(60))

print("===")
l.show()
l.showRev()