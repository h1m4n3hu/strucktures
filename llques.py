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