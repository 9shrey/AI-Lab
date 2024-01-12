from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DFSFnc(self,vertex, visited):
		visited.add(vertex)
		print(vertex, end= ' ')
		for n in self.graph[vertex]:
			if n not in visited:
				self.DFSFnc(n, visited)
				
	def DFS(self,v):
		visited = set()
		self.DFSFnc(v,visited)

if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Depth First Traversal (starting from vertex 2)")
	 
	g.DFS(2)
	print()