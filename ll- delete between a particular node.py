class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head
            print("Head ==>", end=" ")
            while (temp):
                print(temp.data, "==>", end=" ")
                temp = temp.next
            print("Null", end="\n\n")

    def delete_Particular_Node(self, position):
        prev = self.head
        temp = prev.next
        if position == 1:
            self.head = prev.next
            prev.next = None
        elif position < 1 and position - int(position) != 0:
            print("Position should be greater than or equal 1 and it have to be integer.")
        else:
            for i in range(1, position - 1):
                temp = temp.next
                prev = prev.next

            prev.next = temp.next
            temp.next = None

    def Length(self, count):
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


obj = SingleLinkedList()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
obj.display()
obj.delete_Particular_Node(1.7)
obj.display()
obj.delete_Particular_Node(
    int(input(f"Enter the position of node to delete (The linked list conisit of {obj.Length(0)} elements):")))
obj.display()