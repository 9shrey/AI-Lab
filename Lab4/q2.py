class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self, v):
        visited = set()
        queue = [v]
        visited.add(v)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for n in self.graph[vertex]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)")
    g.BFS(2)
    print()
