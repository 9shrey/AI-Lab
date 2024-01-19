class Graph:
	def __init__(self):
		self.adj_list={}

	def add_edge(self,node,connections):
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
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(4, 1)
    g.add_edge(4, 5)
    g.add_edge(5, 3)

    g.check_cyclic()

