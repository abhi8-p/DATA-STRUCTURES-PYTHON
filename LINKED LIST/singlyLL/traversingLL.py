# you are provided with the head of the LL all you have to do is print all the elements present in the LL

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
    print("\nin main")

# time complexity = θ(n), auxillary space θ(1)
def printLL(head):
    curr = head
    while curr!= None:
        print(curr.key,end ='   ')
        curr = curr.next

#driver code......
if __name__ == '__main__':
    main()
    