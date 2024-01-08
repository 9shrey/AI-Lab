class Graph:
    def __init__(self):
        self.list = {}
        self.nodes = set()
    def add(self, from_vertex, to_vertex,weight):
        self.nodes.add(from_vertex)
        self.nodes.add(to_vertex)

        if from_vertex in self.list:
            self.list[from_vertex].append((to_vertex,weight))
        else:
            self.list[from_vertex] = [(to_vertex,weight)]
    
    def print_list(self):
        print("List:")
        for node in self.list:
            for i in range(len(self.list[node])):
                for j in range(len(self.list[node][i])-1):
                    print(f"({node}->{self.list[node][i][j]},{self.list[node][i][j+1]})", end="\t")
            print()
            
def main():
    graph = Graph()
    graph.add(0, 1, 6)
    graph.add(1, 2, 7)
    graph.add(2, 0, 5)
    graph.add(2, 1, 4)
    graph.add(3, 2, 10)

    graph.print_list()

if __name__ == "__main__":
    main()