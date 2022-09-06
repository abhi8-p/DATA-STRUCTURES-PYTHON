from ast import main
"""
there are n nodes for every node it does constant work so 
Time complexity = theta(n) 
Auxillary space = theta(h), h being the height of the parameter
"""

class Node:
    def __init__(self,k):
        self.key = k
        self.right = None
        self.left = None


def main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    inorderTraversal(root)

def inorderTraversal(root):
    if root != None:
        inorderTraversal(root.left)
        print(root.key)
        inorderTraversal(root.right)
    

if __name__ == '__main__':
    main()