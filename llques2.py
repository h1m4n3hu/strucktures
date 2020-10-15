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

l=LList()
l.push(Node(11))
l.push(Node(22))
l.push(Node(33))
l.push(Node(44))
l.push(Node(55))
l.push(Node(66))
l.push(Node(77))
l.push(Node(88))
l.pair_swap()

l.show()