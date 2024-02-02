class Graph:
    def __init__(self):
        self.graph = {}
        self.list = []

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
        if v in self.list:
            print("Cyclic Graph")
            exit(0)
        self.list.append(v)

    def BFS(self, v):
        visited = set()
        queue = [v]

        while queue:
            vertex = queue.pop(0)
            self.list.append(vertex)
            for n in self.graph[vertex]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)

        print("Acyclic Graph")

if __name__ == "__main__":
    g = Graph()
#     g.addEdge(3, 1)
#     g.addEdge(1, 4)
#     g.addEdge(4, 5)
#     g.addEdge(5, 6)
#     g.addEdge(2, 3)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print()
    g.BFS(2)
    print()
