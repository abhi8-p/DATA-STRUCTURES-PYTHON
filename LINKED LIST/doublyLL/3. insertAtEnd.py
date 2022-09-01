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
    print("Before Insertion") 
    printLL(head)
    key = int(input("\nEnter the value you want to enter at end: "))
    head = insertEnd(head,key)
    print("After Insertion ")
    printLL(head)
    

def printLL(head):
    if head == None :
        return
    curr = head
    while curr != None :
        print(curr.key,end = " ")
        curr =curr.next 

#time complexity = O(n)
def insertEnd(head,key):
    temp = Node(key)
    if head == None:
        temp = Node(key)
        return temp
    curr = head 
    while curr.next != None:
        curr = curr.next
    curr.next = temp 
    temp.prev = curr
    return head


if __name__=='__main__':
    main()