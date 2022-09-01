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
    print("Before Deletion\n")
    printLL(head)
    head = deleteFirstNode(head)
    print("\nAfter Deletion")
    printLL(head)

def printLL(head):
    curr = head
    while curr!= None:
        print(curr.key,end ='   ')
        curr = curr.next


def deleteFirstNode(head):
    '''curr = head
    head = curr.next
    return head'''
    if head == None:
        return None 
    else:
        return head.next


#driver code......
if __name__ == '__main__':
    main()
    

