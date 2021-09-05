class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph_arr=[[0]*self.vertices for i in range(self.vertices)]
        print(self.graph_arr)

    def add_edge(self,src,dst):
            self.graph_arr[src][dst]=1
            self.graph_arr[dst][src]=1
            


    def print_graph(self):
        r,c=len(self.graph_arr),len(self.graph_arr[0])
        for i in range(r):
            for j in range(c):
                print(self.graph_arr[i][j],end=" ")
            print()



v=5
graph=Graph(v)
graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(1, 4)
# graph.add_edge(2, 3)
# graph.add_edge(3, 4)
 
graph.print_graph() 