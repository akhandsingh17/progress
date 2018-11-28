class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def countunival(self,root,count):

        if root is None:
            return True

        left = self.countunival(root.left,count)
        right = self.countunival(root.right,count)

        if left == False or right == False:
            return False

        # if left is not None and data is not matching with root.
        if root.left and root.left.data != root.data:
            return False

        if root.right and root.right.data != root.data:
            return False

        count[0]+=1
        return True

    def counting(self,root):
        count=[0]
        self.countunival(root,count)
        return count[0]



root=Node(0)
root.left=Node(1)
root.right=Node(0)
root.right.left=Node(1)
root.right.right=Node(0)
root.right.left.left=Node(1)
root.right.left.right=Node(1)
## Count Unival Tree's
print root.counting(root)
