# for every kth iteration it will reach k+1 th node using for loop
#Let there are 5 nodes so, while curr!= None: will have 5 iterations, but while curr.next != None will have 4 iterations 
#driver code....
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
    printLL(head)
    print()
    KthNode(head,4)
    print("\nin main")

# time complexity = θ(n), auxillary space θ(1)
def printLL(head):
    curr = head
    while curr!= None:
        print(curr.key,end ='   ')
        curr = curr.next

def KthNode(head,k):
    curr = head
    for i in range(4):
        print(i,curr.key)
        curr = curr.next
    print(curr.key)

def insertKthNode(head,key):
    pass
#driver code......
if __name__ == '__main__':
    main()
    