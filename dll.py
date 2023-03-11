class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class singlelinkedlist:
    def __init__(self):
        self.head=None

    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next= temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

ob= singlelinkedlist()
n=Node(100)
ob.head=n
n1=Node(200)
n.next=n1
n2=Node(300)
n1.next=n2
n3=Node(400)
n2.next=n3
n4=Node(500)
n3.next=n4
print("before inserction")
ob.display()
print("")
ob.insert_position(3,100)
ob.display()