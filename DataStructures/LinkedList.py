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
        print("\n")

    def insertAtBeginning(self, data):
        if self.headval == None:
            # the linked list is empty
            # hence make new node and set headval
            nodeToInsert = Node(data)
            self.headval = nodeToInsert
        else:
            # case where the list is not empty
            # the headval points to the next node
            # store that reference somewhere
            # storing it in nodeLink
            nodeLink = self.headval
            # creating the new node
            newNode = Node(data)
            # setting the head of list to the created node
            self.headval = newNode
            # setting nextval of new node to the previous nodes in the
            newNode.nextval = nodeLink

    def insertAtEnd(self, data):
        if self.headval == None:
            self.insertAtBeginning(data)
        else:
            # traverse till the end of the list
            currentNode = self.headval
            while currentNode.nextval != None:
                currentNode = currentNode.nextval
            # currentNode now points to the last node
            # create the new node
            newNode = Node(data)
            # adding new node to the end of the list
            currentNode.nextval = newNode

    def insertAfterKthPosition(self, data, k):
        if self.headval == None:
            self.insertAtBeginning(data)
        else:
            # check if there are K nodes and traverse to the Kth node
            currentNode = self.headval
            count = 1
            # check if currentNode is null
            while currentNode != None and count < k:
                # increment count
                count += 1
                # go to the next node in the list
                currentNode = currentNode.nextval
            # check if loop terminated due to count or
            # because K nodes aren't present
            # print("current node value is: ", currentNode.dataval)
            if count == k:
                # currentNode is pointing to the Kth node
                # make new node and add it to Kth node
                newNode = Node(data)
                # storing the node links in a temporary node
                tempNode = currentNode.nextval
                # setting the Kth node to point to the new node
                currentNode.nextval = newNode
                # setting new node to point to the node links
                newNode.nextval = tempNode
            elif currentNode == None:
                print("K nodes not present in the list. Appending to the end of the list")
                self.insertAtEnd(data)

    def deleteAtBeginning(self):
        # if the list is empty return
        if self.headval == None:
            print("List is empty\n")
            return
        else:
            # we first have to preserve the link to next node
            # from the first node
            nodeLinks = self.headval.nextval
            # delete the first node
            firstNode = self.headval
            del(firstNode)
            # setting the headval to the nodelinks preserved earlier
            self.headval = nodeLinks

    def deleteAtEnding(self):
        if(self.headval == None):
            print("List is empty\n")
            return
        else:
            # traverse till the second last node
            # to do this we do the following:
            # first set the currentNode to the start of the list
            currentNode = self.headval

            while currentNode.nextval != None:
                # the next to next node is null
                if currentNode.nextval.nextval == None:
                    # this is the nodde we require
                    # so we break here
                    break
                # else we continue
                currentNode = currentNode.nextval
            # check if current node is headval
            # ie there is only one node in the list
            if currentNode.nextval == None:
                self.headval = None
                del(currentNode)
            else:
                # we now get a ref to the last node
                lastNode = currentNode.nextval
                # setting the current Node to null to break the chain
                currentNode.nextval = None
                # deleting  the separated link
                del(lastNode)


if __name__=="__main__":
    try:
        list1 = SLinkedList()
        num = int(input("Enter num\n"))
        list1.insertAtBeginning(num)
        list1.listprint()
        num = int(input("Enter num\n"))
        list1.insertAtBeginning(num)
        list1.listprint()
        num = int(input("Enter num\n"))
        list1.insertAtEnd(num)
        list1.listprint()
        num = int(input("Enter num\n"))
        list1.insertAtEnd(num)
        list1.listprint()
        list1.deleteAtBeginning()
        list1.listprint()
        list1.deleteAtEnding()
        list1.listprint()

    except ValueError as e:
        print("Enter a valid number!")
        print(e)



    # num = int(input("Enter num\n"))
    # k = int(input("Enter k value: \n"))
    # list1.insertAfterKthPosition(num, k)
    # list1.listprint()

    # print(" enter num of entries: \n")
    # n = int(input())
    # currentLastNode = None
    # for i in range(n):

    #     num = int(input("Enter num"))
    #     if list1.headval == None:
    #         firstNode = Node(num)
    #         list1.headval = firstNode
    #         currentLastNode = list1.headval
    #     else:
    #         # creating the new Node
    #         newNode = Node(num)
    #         currentLastNode.nextval = newNode
    #         currentLastNode = newNode
    # print("\n")
    # # printing list
    # list1.listprint()


