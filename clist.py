class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Clist:
    def __init__(self):
        self.head=None

    def append(self,value):
        if self.head is None:
            self.head=value
            self.head.next=self.head
        else:
            first=self.head
            while first:
                first=first.next
                if first==self.head:
                    break       #dekh keeee :~~)


    def show(self):
        first=self.head
        while first:
            print(first.value)
            first=first.next
            if first==self.head:
                break


l=Clist()
l.append(Node("a"))
l.append(Node("b"))
l.append(Node("c"))

l.show()