class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def main():
    temp1 = Node(20)
    temp2 = Node(30)
    temp3 = Node(40)
    print("new node",Node(50))
    temp1.next = temp2
    temp2.next = temp3
    print("\nin main")

def main2():
    #another way of implementing LINKED LIST
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    print("\nIN main2")
if __name__ == '__main__':
    main()
    main2()