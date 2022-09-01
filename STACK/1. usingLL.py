# here we can decide from which end to choose as the stack end , we here use head as stack end
from email import header


class Node:
    def __init__ (self,key):
        self.key = key 
        self.next = None

class MyStack():
    def __init__(self):
        MyStack.head = None
        MyStack.size = 0
    
    def push(self,key):
        if MyStack.head == None:
            MyStack.head = Node(key)
            MyStack.size = 1
        else:
            temp = Node(key)
            temp.next = MyStack.head
            MyStack.head = temp
            MyStack.size = MyStack.size + 1
    
    def pop(self):
        if MyStack.head == None:
            print("Underflow")
        else:
            MyStack.head = MyStack.head.next
            MyStack.size = MyStack.size - 1
    def peek(self):
        if MyStack.head == None:
            print("Underflow")
        else:
            print(MyStack.head.key)

    def isEmpty(self):
        if MyStack.head == None:
            print("Yes")
        else:
            print("No")
    def sizeo(self):
        print(MyStack.size)



   

def main():
    s = MyStack()
    s.push(64)
    s.pop()
    s.push(59)
    s.sizeo()
    s.peek()

if __name__ == '__main__':
    main()
