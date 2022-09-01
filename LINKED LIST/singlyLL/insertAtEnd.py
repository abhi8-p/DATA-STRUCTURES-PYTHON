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
    pos = int(input("Enter the position to insert a key"))
    key = int(input("Insert a key"))
    head = insertPos(head,pos,key)
    printLL(head)
    print("\nin main")

def printLL(head):
    curr = head
    print("\nLINKED LIST: ")
    while curr!= None:
        print(curr.key,end ='   ')
        curr = curr.next
#driver code......

# time complexity = O(n),auxillary space: O(1)  
def insertPos(head,pos,key):
    curr = head
    if pos ==1:
        temp = Node(key)
        temp.next = head.next
        head = temp
        return head
    for i in range (pos -2):
        curr = curr.next
        if curr == None:
            return head 
    temp.next = curr.next
    curr.next = temp 
    return head

    

if __name__ == '__main__':
    main()