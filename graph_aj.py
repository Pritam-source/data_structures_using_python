class Node:
    def __init__(self,node):
        self.node = node
        self.next = None
    
    
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph_arr=[None]*self.vertices

    def add_edge(self,src,dst):
        node=Node(dst)
        node.next=self.graph_arr[src]
        self.graph_arr[src]=node

        node = Node(src)
        node.next = self.graph_arr[dst]
        self.graph_arr[dst] = node
    
    def print_graph(self):
        for i in range(self.vertices):
            print("{}:".format(i),end="")
            temp=self.graph_arr[i]
            while temp:
                print("{} ->".format(temp.node),end="")
                temp=temp.next
            print("\n")
v=5
graph = Graph(v)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
 
graph.print_graph()         

