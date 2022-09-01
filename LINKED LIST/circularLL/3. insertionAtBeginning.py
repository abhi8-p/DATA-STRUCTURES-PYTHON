''' in the while condition if you write curr.next ! = head then it will give you a AttributeError for empty LL.
So you should always write curr != head to avoid AttributeError
'''

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
    print("Before Insertion: ")
    printLL(head)
    key = int(input("\nEnter a key you want to enter"))
    head = insertBeginning(head,key)
    print("\nAfter Insertion: ")
    printLL(head)
    print("\nAfter constant time Insertion: ")
    printLL(head)

def printLL(head):
    if head == None:
        return
    print(head.key,end = ' ')
    curr = head.next 
    while curr!=head:
        print(curr.key,end = ' ')
        curr = curr.next
    
def insertBeginning(head,key):
    temp = Node(key)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr= curr.next
    curr.next = temp
    temp.next = head
    return temp

def insertBeginningConstantTime(head,key):
    #the basic idea behind this is you insert the data at the 2nd position and then swap the data with the first position. Check Onenote'
    temp = Node(key)
    if head == None:
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    temp.key,head.key = head.key,temp.key
    return head

if __name__ == '__main__':
    main()