# as we dont traverse through the head and Kth position so we loop for k-2 times, such that for k-2th iteration we reach the previous element of that we are going to delete

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
    k = int(input("Enter the position to be deleted."))
    print("before deleting head ")
    printLL(head)
    print("\nAfter deletion")
    head = deleteKth(head,k)
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

def deleteKth(head,k):
    curr = head
    if head == None:
        return 
    elif k == 1:
        return deleteHead(head) 
    for i in range(k-2):
        curr = curr.next
    curr.next = curr.next.next

if __name__ == '__main__':
    main()

