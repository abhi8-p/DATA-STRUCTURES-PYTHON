class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def main():
    temp1 = Node(20)
    temp2 = Node(30)
    temp3 = Node(40)
    temp4 = Node(60)
    temp5 = Node(70)
    temp1.next = temp2
    temp2.next = temp3
    temp3.next = temp4
    temp4.next = temp5
    head = temp1

    print("before deletion\n")
    printLL(head)
    head = deleteLastNode(head)
    print("\nAfter deletion")
    printLL(head)

def printLL(head):
    curr = head
    print("\nLINKED LIST: ")
    while curr!= None:
        print(curr.key,end ='   ')
        curr = curr.next
#driver code......

# time complexity = O(n),auxillary space: O(1)  
def deleteLastNode(head):
    if head == None:
        return None
    if head.next == None:
        return None 
    curr = head
    while curr.next.next!= None:
        curr = curr.next
    curr.next = None
    return head
    

    

if __name__ == '__main__':
    main()