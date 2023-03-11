def delete_start(self):
    temp=self.head
    temp.next.prev=None
    self.head=temp.next
    temp.next=None