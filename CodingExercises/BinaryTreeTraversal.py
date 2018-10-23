class Node:

    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

## Insert Data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


## Print Tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print (self.data),
        if self.right:
            self.right.PrintTree()

## In-order Tree Traversal
## Left ---> Root ---> Right
    def inorderTraversal(self,root):
        res1=[]
        if root:
            res1=self.inorderTraversal(root.left)
            res1.append(root.data)
            res1=res1+self.inorderTraversal(root.right)
        return res1


## Pre-order Tree Traversal
## Root --> Left --Right

    def preorderTraversal(self,root):
        res2=[]
        if root:
            res2.append(root.data)
            res2=res2 + self.preorderTraversal(root.left)
            res2=res2 + self.preorderTraversal(root.right)
        return res2

## Post-order Tree Traversal
## Left --> Right --Root

    def postorderTraversal(self,root):
        res3=[]
        if root:
            res3=self.postorderTraversal(root.left)
            res3=res3+self.postorderTraversal(root.right)
            res3.append(root.data)
        return res3

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))






