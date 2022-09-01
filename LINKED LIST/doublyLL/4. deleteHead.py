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
    head = deleteHead(head)
    print("\nAfter Deletion ")
    printLL(head)
    

def printLL(head):
    if head == None :
        return
    curr = head
    while curr != None :
        print(curr.key,end = " ")
        curr =curr.next 

#time complexity = O(1)
def deleteHead(head):
    if head == None:
        return None
    if head.next == None:
        return None
    head = head .next 
    head.prev = None
    return head


if __name__=='__main__':
    main()