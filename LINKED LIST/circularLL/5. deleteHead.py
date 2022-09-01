

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None 

def main():
    head = Node(10)
    head.next=Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = head
    print("before deleting head ")
    printLL(head)
    print("\nAfter deletion")
    head = deleteHead(head)
    printLL(head)

def printLL(head):
    if head.next == None:
        return
    print(head.key,end =' ')
    curr = head.next 
    while curr!=head:
        print(curr.key,end = ' ')
        curr = curr.next
    
def deleteHead(head):
    head.key = head.next.key
    head.next = head.next.next
    return head    



if __name__ == '__main__':
    main()