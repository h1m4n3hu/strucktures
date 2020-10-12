class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Clist:
    def __init__(self):
        self.head=None

    def append(self, value):
        if not self.head:
            self.head=value
            self.head.next=self.head
        else:
            first=self.head
            while first:
                first=first.next
                if first.next==self.head:
                    break
            first.next=value
            value.next=self.head

    def prepend(self,value):
        if not self.head:
            value.next=value
        else:
            first=self.head
            k=first
            while first.next!=self.head:
                first=first.next
            first.next=value
            value.next=k
        self.head=value

    def pop(self):
        first=self.head
        while first.next!=self.head:
            last=first
            first=first.next
        last.next=self.head
        first.next=None

    def poptop(self):
        first=self.head
        second=first.next
        first.next=None
        self.head=second
        k=self.head
        while k.next:
            print(k.value,"k")
            last=k
            k=k.next
            if k==self.head:
                break
        last.next=second

    def remove(self,pos):
        i=0
        first=self.head.next
        while i<pos-1:
            prev=first
            first=first.next
            i+=1
        prev.next=first.next
        first.next=None

    def index(self,data):
        i=0
        first=self.head
        while first:
            if first.value==data:
                return i
            first=first.next
            i+=1
            if first==self.head:
                break

    def delete(self,data):
        ii=self.index(data)
        self.remove(ii)

    def show(self):
        first=self.head
        while first:
            print(first.value)
            first=first.next
            if first==self.head:
                break
        #while first.next!=self.head:
            #print(first.value)
            #first=first.next

"""    def show(self):
        first=self.head
        while first.next!=self.head:
            print("h")
            first=first.next

    def show(self):
        first=self.head
        while first:
            print(first.value)
            first=first.next
            if first==self.head:
                break"""


l=Clist()
l.append(Node("a"))
l.append(Node("b"))
l.append(Node("c"))
l.append(Node("d"))
l.append(Node("e"))
l.append(Node("f"))
l.delete("c")

l.show()