class Node:
    def __init__(self,key):
        self.left= None
        self.right= None
        self.val= key
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)
def printPostorder(root):
    if root:
        print(root.val,end=" ")
        printPostorder(root.left)
        printPostorder(root.right)
def printPreorder(root):
    if root:
        print(root.val,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

root=Node(1)
root.left= Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("preorder:")
printPreorder(root)
print()
print("inorder:")
printInorder(root)
print()
print("postorder:")
printPostorder(root)
print()