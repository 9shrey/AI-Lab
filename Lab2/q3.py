class Graph:
    def __init__(self):
        self.adj_list = {}
        self.nodes = set()

    def add(self, node_from, node_to):
        self.nodes.add(node_from)
        self.nodes.add(node_to)

        if node_from in self.adj_list:
            self.adj_list[node_from].append((node_to))
        else:
            self.adj_list[node_from] = [(node_to)]

    def print_adj_list(self):
        print("Adjacency List:")
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

    def print_adj_matrix(self):
        print("\nAdjacency Matrix:")
        matrix = []
        for _ in range(len(self.nodes)):
            row = [0] * len(self.nodes) 
            matrix.append(row)
            
        sorted_nodes = sorted(self.nodes)
        node_index = {}
        for i, node in enumerate(sorted_nodes):
            node_index[node] = i

        for node_from, i in self.adj_list.items():
            for node_to in i:
                matrix[node_index[node_from]][node_index[node_to]] = 1
        
        for row in matrix:
            print(row)


def main():
    graph = Graph()
    graph.add('A', 'B')
    graph.add('A', 'C')
    graph.add('A', 'E')
    graph.add('E', 'C')
    graph.add('D', 'C')
    graph.add('E', 'A')
    graph.add('B', 'A')
    graph.add('B', 'C')
    graph.add('C', 'B')
    graph.add('C', 'D')
    graph.add('C', 'A')
    graph.add('C', 'E')

    graph.print_adj_list()
    graph.print_adj_matrix()


if __name__ == "__main__":
    main()
