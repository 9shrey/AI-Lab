class Graph:
	def __init__(self):
		self.adj_list={}

	def addEdge(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		if connections not in self.adj_list:
			self.adj_list[connections]=[]
		
		self.adj_list[node].append(connections)

	def cyclic(self,node,visited,path):
		visited[node]=True
		path[node]=True
		for neighbour in self.adj_list[node]:
			if visited[neighbour]==False:
				if self.cyclic(neighbour,visited,path)==True:
					return True
			elif path[neighbour]==True:
				return True

		path[node]=False
		return False

	def check_cyclic(self):
		visited=[False]*len(self.adj_list)
		path=[False]*len(self.adj_list)
		for vertex in self.adj_list:
			if self.cyclic(vertex,visited,path)==True:
				print("Cycle exists")
				return
		print("Acyclic Graph")

			
if __name__ == '__main__':
    g = Graph()
      # g.addEdge(3, 1)
    # g.addEdge(1, 4)
    # g.addEdge(4, 5)
    # g.addEdge(5, 6)
    # g.addEdge(2, 3)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.check_cyclic()
