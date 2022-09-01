
# time complexity = θ(1), auxiliary space = θ(1)
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
    print("Before insertion ")
    printLL(head)
    print("\nAfter Insertion")
    head = insertEnd(head,50)
    printLL(head)

def printLL(head):
    if head == None:
        return
    print(head.key,end =' ')
    curr = head.next 
    while curr != head:
        print(curr.key,end = ' ')
        curr = curr.next
    
def insertEnd(head,key):
    temp = Node(key)
    temp.next = head.next
    head.next = temp 
    temp.key,head.key = head.key,temp.key 
    return temp 
if __name__ == '__main__':
    main()
    # print("Creating an Empty LL\n")
    # emptyLL()