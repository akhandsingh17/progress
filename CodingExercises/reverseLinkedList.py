
## How to reverse a linked list
# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)


class Node:

    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinklist:

    def __init__(self):
        self.headval=None



    def printlist(self):
        printval=self.headval
        while printval is not None:
            print (printval.dataval)
            printval=printval.nextval


    def addatbegin(self,newdata):
        Newnode=Node(newdata)
        Newnode.nextval=self.headval
        self.headval=Newnode


    def addatend(self,newdata):
        Newnode=Node(newdata)
        if self.headval is None:
            self.headval=Newnode
            return
        last=self.headval
        while (last.nextval):
            last=last.nextval
        last.nextval=Newnode


    def reverse(self):
        prev=None
        next=None
        curr=self.headval
        while(curr is not None):
            next=curr.nextval
            curr.nextval=prev
            prev=curr
            curr=next
        self.headval=prev


list = SLinklist()
N0 = Node("Mon")
N1 = Node("Tue")
N2 = Node("Wed")
N3 = Node("Thu")
N4 = Node("Fri")

list.headval=N0
N0.nextval=N1
N1.nextval=N2
N2.nextval=N3
N3.nextval=N4
#list.addatbegin("Sun")
#list.addatend("Sat")
print "Given Linked List:"
print list.printlist()

list.reverse()
print "\nReversed Linked List:"
print list.printlist()



