import random

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Playlist:
    def __init__(self):
        self.head=None
        self.i=0

    def add_song(self,data):
        if not self.head:
            new=Node(data)
            self.head=new
        else:
            new=Node(data)
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new
            new.prev=cur

    def remove_song(self,data):
        if self.head.data==data and self.head.next:
            temp=self.head.next
            temp.prev=None
            self.head.next=None
            temp=self.head
        elif self.head.data==data and not self.head.next:
            self.head=None
        else:
            var=self.head
            pre=None
            while var:
                if var.data==data and var.next:
                    temp=var.next
                    pre.next=temp
                    temp.prev=pre
                    var.next=None
                    var.prev=None
                elif var.data==data and not var.next:
                    pre.next=None
                pre=var
                var=var.next

    def show_list(self):
        if not self.head:
            print("No Songs!")
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def play(self):
        if self.head:
            if self.i==0:
                print("Playing",self.head.data)
            else:
                k=0
                temp=self.head
                while k<self.i:
                    k+=1
                    temp=temp.next
                print("Playing",temp.data)
        else:
            print("No Songs Found!")

    def go_next(self):
        self.i=(self.i+1)%self.len_songs()
        self.play()

    def go_prev(self):
        self.i=(self.i-1)%self.len_songs()
        self.play()

    def len_songs(self):
        k=0
        temp=self.head
        while temp:
            k+=1
            temp=temp.next
        return k

    def shuffle(self):
        if not self.head:
            print("No Songs Found!")
            return
        l=[]
        temp=self.head
        while temp:
            l.append(temp.data)
            temp=temp.next
        random.shuffle(l)
        cur=self.head
        i=0
        while cur:
            cur.data=l[i]
            i+=1
            cur=cur.next
        print("Playlist Shuffled!")

    def sort(self):
        if not self.head:
            print("No Songs Found!")
            return
        l=[]
        temp=self.head
        while temp:
            l.append(temp.data)
            temp=temp.next
        l.sort()
        cur=self.head
        i=0
        while cur:
            cur.data=l[i]
            i+=1
            cur=cur.next
        print("Playlist Sorted!")

# p=Playlist()
# p.head=Node(1)
# p.add_song(2)
# p.add_song(4)
# p.show_list()