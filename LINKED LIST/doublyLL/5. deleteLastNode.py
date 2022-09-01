class Node:
    def __init__(self,key):
        self.prev = None 
        self.next = None
        self.key = key

def main():
    head = Node(10)
    temp1 = Node(20)
    temp2 = Node(30)
    head.next = temp1 
    temp1.prev = head 
    temp1.next = temp2
    temp2.prev = temp1
    print("Before Deletion") 
    printLL(head)
    head = deleteEnd(head)
    print("\nAfter Deletion ")
    printLL(head)
    

def printLL(head):
    if head == None :
        return
    curr = head
    while curr != None :
        print(curr.key,end = " ")
        curr =curr.next 

#time complexity = O(n)
def deleteEnd(head):
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
    temp = curr.next
    temp.prev = None
    curr.next = None
    return head 
    


if __name__=='__main__':
    main()