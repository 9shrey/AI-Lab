class Graph:
    def __init__(self):
        self.list = {}
        self.nodes = set()
    def add(self, from_vertex, to_vertex):
        self.nodes.add(from_vertex)
        self.nodes.add(to_vertex)

        if from_vertex in self.list:
            self.list[from_vertex].append((to_vertex))
        else:
            self.list[from_vertex] = [(to_vertex)]
    
    def print_list(self):
        print("List:")
        for node in self.list:
            for i in range(len(self.list[node])):
                print(f"({node}->{self.list[node][i]})", end="\t")
            print()
            
def main():
    graph = Graph()
    graph.add(0, 1)
    graph.add(3, 1)
    graph.add(3, 5)
    graph.add(4, 2)
    graph.add(1, 3)

    graph.print_list()

if __name__ == "__main__":
    main()