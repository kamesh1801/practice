'''insert at beginning
insert btw nodes
insert at end'''
'''insert at beginning
step1: create a new node which u want to insert
step2: make the new node point to current head noide
step3:make ur new node as head node
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singleLL:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,'-->',end=" ")
                temp=temp.next
ob=singleLL()

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
ob.insert_end(100)
ob.display()
