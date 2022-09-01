
# time complexity = θ(n), auxiliary space = θ(1)
class Node:
    def __init__(self,key = None):
        self.key = key
        self.next = None 

def main():
    head = Node(10)
    head.next=Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = head
    print("LINKED LIST: ")
    printLL(head)
'''
def emptyLL():
    head = Node()
    head.next = Node()
    print("LINKED LIST: ")
    if head == None:
        print(1)
    printLL(head)
'''
def printLL(head):
    if head == None:
        return
    print(head.key,end =' ')
    curr = head.next 
    while curr != head:
        print(curr.key,end = ' ')
        curr = curr.next
    
if __name__ == '__main__':
    main()
    # print("Creating an Empty LL\n")
    # emptyLL()