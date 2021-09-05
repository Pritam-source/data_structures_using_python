class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        
class Tree:
    def createNode(self,data):
        return Node(data)

    def Insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left=self.Insert(node.left,data)
        else:
            node.right=self.Insert(node.right,data)
        return node

    def In_order(self,root):
        if root is not None:
            self.In_order(root.left)
            print(root.data)
            self.In_order(root.right)
        

tree =Tree()
root=tree.createNode(5)
tree.Insert(root,2)
tree.Insert(root,10)
tree.Insert(root,7)
tree.Insert(root,15)
tree.Insert(root,12)
tree.Insert(root,20)
tree.Insert(root,30)
tree.Insert(root,6)
tree.Insert(root,8)
tree.In_order(root)