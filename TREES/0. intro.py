from ast import main


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

if __name__ == '__main__':
    main()