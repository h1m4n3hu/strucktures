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
            #new_node=data
            #cur=self.head
            first=self.head
            while first:
                first=first.next
                if first.next==self.head:
                    break
            first.next=value
            value.next=self.head

    def show(self):
        first = self.head
        while first:
            print(first.value)
            first=first.next
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
l.append(Node("e"))
l.append(Node("f"))

l.show()