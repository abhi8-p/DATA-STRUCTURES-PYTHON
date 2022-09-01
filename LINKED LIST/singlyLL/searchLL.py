# you have to search the element in the LL,if element is present then return the index of the element or else return -1

#driver code..............
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
    print(searchLL(head,712))

# time complexity = θ(n), auxillary space θ(1)
def searchLL(head,x):
    curr = head
    pos = 1
    while curr!= None:
        if curr.key == x:
            return pos
        pos = pos +1
        curr = curr.next
    return -1

#driver code......
if __name__ == '__main__':
    main()
    