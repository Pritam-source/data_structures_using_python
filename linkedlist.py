class Node:
    def __init__(self,data):
        self.data=data
        self.next =None
        
class Linkedlist:
    def __init__(self):
        self.head=None

    def Insert_begining(self,data):
        if self.head is None:
            self.head=data
        else:
            data.next=self.head
            self.head=data
    def Insert_end(self,data):
        if self.head is None:
            self.head=data
        else:
            last=self.head
            while (last.next):
                last=last.next
            last.next=data
    # def Insert_index(self,data):
    #     if self.head is None:
    #         self.head=data
    #     else:
            

    def show(self):
        node=self.head
        while node is not None:
            print(node.data)
            node=node.next





headNode=Node(6)
ll=Linkedlist()
ll.Insert_begining(headNode)
ele2=Node(7)
ll.Insert_begining(ele2)
ele3=Node(8)
ll.Insert_begining(ele3)
ele4=Node('pritam')
ll.Insert_begining(ele4)
ele5=Node(5)
ll.Insert_end(ele5)
ll.show()
