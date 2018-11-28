class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,traverse):
        if start:
            traverse= traverse + (str(start.data)+'-')
            traverse =  self.preorder(start.left,traverse)
            traverse =  self.preorder(start.right,traverse)
        return  traverse


    def postorder(self,start,traverse):
        if start:
            traverse =  self.preorder(start.left,traverse)
            traverse =  self.preorder(start.right,traverse)
            traverse= traverse + (str(start.data)+'-')
        return traverse

    def inorder(self,start,traverse):
        if start:
            traverse =  self.preorder(start.left,traverse)
            traverse= traverse + (str(start.data)+'-')
            traverse =  self.preorder(start.right,traverse)
        return traverse

    def getlist(self,str):
        res=[]
        for chr in str:
            if chr != '-':
                res.append(chr)
            else:
                continue
        return res


    def print_tree(self,traversetype):
        if traversetype == 'preorder':
            print "\n preorder"
            return self.preorder(self.root,'')


        if traversetype == 'postorder':
            print "\n postorder"
            return self.postorder(self.root,'')

        if traversetype == 'inorder':
            print "\n inorder"
            return self.inorder(self.root,'')

def main():

    tree=BinaryTree(0)
    tree.root.left=Node(1)
    tree.root.right=Node(0)
    tree.root.right.left=Node(1)
    tree.root.right.right=Node(0)
    tree.root.right.left.left=Node(1)
    tree.root.right.left.right=Node(1)
    path=tree.print_tree('preorder')
    print tree.getlist(path)

if __name__=='__main__':
    main()