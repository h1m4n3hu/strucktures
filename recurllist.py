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

l=LList()
l.push(Node(11))
l.push(Node(22))
l.push(Node(33))
l.push(Node(44))
l.push(Node(55))
l.push(Node(66))
l.push(Node(77))
l.push(Node(88))
l.push(Node(99))


#l.show()