class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev= prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print('linked is empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
    '''def delete(self):       #DELETE AT BEGINNING
        temp=self.head
        self.head=temp.next
        temp.next=None'''


''' def delete(self):    #deletion at end
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None'''
ob=SLL()
n1=Node(200)
ob.head=n1
n2=Node(300)
n1.next=n2
n3=Node(400)
n2.next=n3
ob.display()
#ob.delete()
ob.delete_position(2)
print("")
ob.display()