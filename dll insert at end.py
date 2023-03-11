class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp= self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

l=dll()
n=Node(100)
l.head=n
n1=Node(200)
n1.prev=n
n.next=n1
n2=Node(300)
n2.prev=n1
n2.next=n1
l.display()
print('')
print('after insertion')
l.insert_end()
l.display()