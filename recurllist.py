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

    def altdelete(self):
        k=self.head
        while k and k.next:
            k.next=k.next.next
            k=k.next

    def printalt(self):
        k=self.head
        try:
            while k:
                print(k.value)
                k=k.next.next
            print(k.value)
        except:
            pass

    def recur_alt_print(self,n):
        if n.next:
            print(n.value)
            return self.recur_alt_print(n.next.next)

    def recur_search(self,head,n,i=0):
        if head.value==n:
            print(i)
        if head.next:
            self.recur_search(head.next,n,i+1)

    def recurlen(self,head,i=0):
        if head is None:
            print(i)
        if head:
            self.recurlen(head.next,i+1)

    def rec_index(self,head,value,i=0):
        if head and head.value==value:
            print(i)
        if head:
            self.rec_index(head.next,value,i+1)

    def is_pal(self,head):
        if head.next:                   #########
            self.is_pal(head.next)      #########
        print(head.value)               #########

l=LList()
l.push(Node("r"))
l.push(Node("a"))
l.push(Node("d"))
l.push(Node("e"))
l.push(Node("e"))
l.push(Node("l"))
l.push(Node("s"))
l.rec_index(l.head,"a")

#l.show()