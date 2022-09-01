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
    print("Before Reverse ") 
    printLL(head)
    head = reverseDLL(head)
    print("\nAfter Reverse ")
    printLL(head)
    

def printLL(head):
    if head == None :
        return
    curr = head
    while curr != None :
        print(curr.key,end = " ")
        curr =curr.next 

#time complexity = O(n)
def reverseDLL(head):
    if head == None:
        return None
    if head.next == None:
        return head 
    curr = head
    prev = None
    while curr != None:
        prev = curr 
        curr.next,curr.prev = curr.prev,curr.next
        curr = curr.prev
    return prev


if __name__=='__main__':
    main()