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
        if(printval == None):
            print("List is empty \n")
            return
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


    def deleteKthNode(self, k):

        # to do this we first need to check if there are k nodes
        # we try to traverse to the kth node
        count = 0
        currentNode = self.headval
        # check if list is already empty
        if currentNode == None:
            print("List is empty \n")
            return
        prev2Node = None
        prevNode = None
        # looping through
        while currentNode != None and count < k:
            count += 1
            # prev2Node will hold the (K-1)th node
            prev2Node = prevNode
            # setting prevNode to the current node
            prevNode = currentNode
            # advancing currentNode by 1
            currentNode = currentNode.nextval
        # prevnode now holds the Kth node and currentNode holds K+1th node if they exist
        # check if k nodes are present or not
        if count != k:
            print("K nodes not present\n")
            print("Please enter valid K\n")
            self.listprint()
            return
        # if currentNode is None then
        # the node to be deleted is the last node
        # hence call deleteAtEnd method
        if currentNode == None:
            self.deleteAtEnding()
        else:
            if(prev2Node == None):
                self.deleteAtBeginning()
                return
            # the node we need to delete is
            # is in prevNode
            # storing the node links in a var
            nodeLinks = prevNode.nextval
            # setting (K-1)th node to point to the (K+1)th node
            prev2Node.nextval = nodeLinks

            # deleting the node
            del(prevNode)

    def countKthNode(self ,node, k):
        # if node is null
        if node == None:
            # the linked list is empty
            print("No linked list")
            return -1
        if node.nextval == None:
            # this is the last node in the linked list
            return 1
        else:
            # adding the count returned by the function and adding 1
            # to include the current node as well
            c = 1 + self.countKthNode(node.nextval, k)
            # if the current count is equal
            # to the required value, print the value of the node
            if c == k:
                print("Value of the node: ", node.dataval)
            # return the present count
            return c


def mergeTwoSortedLinkedLists(headOne, headTwo):
    # headOne is the headval of the first linked list
    # headTwo is the headval of the second linked list
    mergedLL = SLinkedList()
    nodeptr1 = headOne
    nodeptr2 = headTwo
    # check if both are None or not
    while nodeptr1 != None and nodeptr2 != None:
        # compare the two values in the present node
        if nodeptr1.dataval >= nodeptr2.dataval:
            # if the second ll has less value we have to insert it into the new linked list
            # so we call insert at end
            mergedLL.insertAtEnd(nodeptr2.dataval)
            # advance to the next node in the second ll
            nodeptr2 = nodeptr2.nextval
        else:
            # if the first node has less data then call insert at end and
            # insert the first lls value
            mergedLL.insertAtEnd(nodeptr1.dataval)
            # advance to the next node in the first ll
            nodeptr1 = nodeptr1.nextval
    # check if there are any other nodes remaining in
    # the other linked lists
    while nodeptr1 != None:
        # if it isnt empty, add each node
        mergedLL.insertAtEnd(nodeptr1.dataval)
        # advance the pointer
        nodeptr1 = nodeptr1.nextval

    while nodeptr2 != None:
        # repeat the same for the second
        # linked list
        mergedLL.insertAtEnd(nodeptr2.dataval)
        nodeptr2 = nodeptr2.nextval
    # return the merged Linked list
    return mergedLL









if __name__=="__main__":
    try:
        list1 = SLinkedList()
        list2 = SLinkedList()
        list1.insertAtEnd(2)
        list1.insertAtEnd(4)
        list1.insertAtEnd(6)
        list1.insertAtEnd(9)
        list1.insertAtEnd(11)
        list1.insertAtEnd(15)
        list2.insertAtEnd(3)
        list2.insertAtEnd(7)
        list2.insertAtEnd(8)
        list2.insertAtEnd(10)
        list2.insertAtEnd(12)
        list2.insertAtEnd(17)
        list2.insertAtEnd(21)
        list1.listprint()
        list2.listprint()
        mLL = mergeTwoSortedLinkedLists(list1.headval, list2.headval)
        mLL.listprint()

        # num = int(input("Enter num\n"))
        # list1.insertAtBeginning(num)
        # list1.listprint()
        # num = int(input("Enter num\n"))
        # list1.insertAtBeginning(num)
        # list1.listprint()
        # num = int(input("Enter num\n"))
        # list1.insertAtEnd(num)
        # list1.listprint()
        # num = int(input("Enter num\n"))
        # list1.insertAtEnd(num)
        # list1.listprint()
        # list1.countKthNode(list1.headval, 2)
        # list1.listprint()


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


