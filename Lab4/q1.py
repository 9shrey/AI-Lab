class Graph:
    def __init__(self, vertices):
        self.graph = {}  # dictionary containing adjacency List
        self.V = vertices 
        
        for i in range(vertices):
            self.graph[i] = []
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def topologicalSort(self):
        in_degree = [0] * self.V
        for i in range(self.V):
            for j in self.graph[i]:
                in_degree[j] += 1
        
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.pop(0)
            
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            
            result.append(node)  # Move this line inside the while loop
            
        print(result)

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(3, 1)
    g.addEdge(2, 3)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    
    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()