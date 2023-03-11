class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,'-->',end=" ")
                temp=temp.next
ob=Sll()

n=Node(10)
ob.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print('before insertion')
ob.display()
print(" ")
print('after insertion')
ob.insert_position(3,100)
ob.display()