class Graph:
	def __init__(self):
		self.adj_mat = []
		self.adj_list = {}
	def add(self, node_from, node_to, value):
		mat = [node_to, value]
		if node_from in self.adj_list:
			self.adj_list[node_from].append(mat)
		else :
			self.adj_list[node_from] = []
				
			self.adj_list[node_from].append(mat)
			print(self.adj_list)
		for i in range(len(self.adj_list)):
			self.adj_mat.append([0]*len(self.adj_list))
		for i in (self.adj_list):
			for j in (self.adj_list[i]):
				self.adj_mat[i-1][j[0]-1] = self.adj_list[j[1]-1]
		print(self.adj_mat)


def main():
	graph = Graph()
	graph.add(1,2,1)
	graph.add(1,3,1)
	graph.add(2,3,3)
	graph.add(3,4,4)
	graph.add(4,1,5)

if __name__ == "__main__":
	main()

