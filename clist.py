class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Clist:
    def __init__(self):
        self.head=None

    def append(self, data):
        if not self.head:
            self.head = data
            self.head.next = self.head
        else:
            new_node = data
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def show(self):
        first = self.head
        while first:
            first=first.next
            print("hh")
            if first==self.head:
                break

"""    def show(self):
    first=self.head
    while first.next!=self.head:
        print("h")
        first=first.next"""



"""    def show(self):
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

l.show()