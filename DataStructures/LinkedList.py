class Node:
    def __init__(self, dataval = None):
        # here dataval is the number that is stored in the linked list
        self.dataval = dataval
        # nextval is like the pointer that points to the next node in the linked list
        self.nextval = None
class SLinkedList:
    def __init__(self):

        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval, end="->")
            printval = printval.nextval

# creating list
list1 = SLinkedList()

print(" enter num of entries: \n")
n = int(input())
currentLastNode = None
for i in range(n):

    num = int(input("Enter num"))
    if list1.headval == None:
        firstNode = Node(num)
        list1.headval = firstNode
        currentLastNode = list1.headval
    else:
        # creating the new Node
        newNode = Node(num)
        currentLastNode.nextval = newNode
        currentLastNode = newNode
print("\n")
list1.listprint()
