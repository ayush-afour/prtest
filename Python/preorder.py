class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key

# A function to do preorder tree traversal 
def printPreorder(root): 
    if root: 
        # First print the data of node 
        print(root.val, end=' ')  # Fix for print function and to avoid newline
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 
  
# Driver code 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    print("Preorder traversal of binary tree is")
    printPreorder(root)

