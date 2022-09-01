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
    key = int(input("Insert a key"))
    insertBeginning(head,key)
    print("\nin main")
#driver code......

# time complexity = O(1),auxillary space: O(1)  
def insertBeginning(head,key):
    temp = Node(key)
    temp.next = head
    printLL(temp)

def printLL(head):
    curr = head
    while curr!= None:
        print(curr.key,end ='   ')
        curr = curr.next

if __name__ == '__main__':
    main() 