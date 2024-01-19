class Graph:
	def __init__(self):
		self.adj_list={}

	def add_edge(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		if connections not in self.adj_list:
			self.adj_list[connections]=[]
		
		self.adj_list[node].append(connections)

	def dfs(self,node,visited,stack):
		visited[node]=True

		for neighbour in self.adj_list[node]:
			if visited[neighbour]==False:
				self.dfs(neighbour,visited,stack)

		stack.append(node)

	def top_sort(self):
		visited=[False]*len(self.adj_list)
		stack=[]

		for vertex in self.adj_list:
			if visited[vertex]==False:
				self.dfs(vertex,visited,stack)

		print(stack[::-1])

if __name__ == '__main__':
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    g.top_sort()