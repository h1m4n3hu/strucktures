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

    def modnod(self,n):
        k=self.head
        res=None
        while k and k.next:
            if k.value%n==0:
                res=k.value
            k=k.next
        print(res)

    def length(self):
        i=1
        k=self.head
        while k and k.next:
            i+=1
            k=k.next
        return i

    def mid(self):
        first=self.head
        k=self.length()
        kk=k//2
        i=0
        while i<kk:
            first=first.next
            i+=1
        print(first.value)

    def last_to_first(self):
        k=self.head
        while k and k.next:
            last=k
            k=k.next
        last.next=None
        k.next=None
        self.place(k)

    def mid_to_head(self):
        k=self.head
        len=self.length()
        i=0
        while i<len//2:
            prev=k
            k=k.next
            i+=1
        mid=k
        prev.next=mid.next
        mid.next=self.head
        self.head=mid

    def isCircular(self):
        k=self.head
        while k and k.next:
            k=k.next
        if k.next==self.head:
            print("circ")
        else:
            print("heh")

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

    def recur_search(self,n,head,i=0):
        if head.value==n:
            print(i)
        if head.next:
            self.recur_search(n,head.next,i+1)

    def count(self,value):
        k=self.head
        i=0
        while k:
            if k.value==value:
                i+=1
            k=k.next
        print(i)

    def insert_list(self,ll,n):
        i=0
        k=self.head
        while i<n:
            prev=k
            k=k.next
            i+=1
        kk=prev.next
        prev.next=ll
        ll.next=kk

    def recur_reverse(self,head):
        print(head.value)
        if head.next:
            self.recur_forward(head.next)

    def recur_forward(self, head):
        if head.next:
            self.recur_forward(head.next)
        print(head.value)

    def recur_del(self,head,n):
        if head.next and head.next.value==n:
            head.next=head.next.next
        if head.next:
            self.recur_del(head.next,n)

def mult(l1,l2):
    f1=l1.head
    s1=""
    f2=l2.head
    s2=""
    while f1:
        s1+=str(f1.value)
        f1=f1.next
    while f2:
        s2+=str(f2.value)
        f2=f2.next
    print(int(s1)*int(s2))

l=LList()
ll=LList()
l.push(Node(3))
l.push(Node(2))
l.push(Node(1))
l.push(Node(1))


#l.show()