class Graph:
    def __init__(self):
        self.adj_list = {}
        self.nodes = set()

    def add(self, node_from, node_to, value):
        self.nodes.add(node_from)
        self.nodes.add(node_to)

        if node_from in self.adj_list:
            self.adj_list[node_from].append((node_to, value))
        else:
            self.adj_list[node_from] = [(node_to, value)]

        if node_to not in self.adj_list:
            self.adj_list[node_to] = []

    def print_adj_list(self):
        print("Adjacency List:")
        for node in self.adj_list:
            print(f"Node {node} is connected to: {self.adj_list[node]}")

    def print_adj_matrix(self):
        print("\nAdjacency Matrix:")
        matrix = [[0] * len(self.nodes) for _ in range(len(self.nodes))]
        node_index = {node: i for i, node in enumerate(sorted(self.nodes))}
        
        for node_from, connections in self.adj_list.items():
            for node_to, value in connections:
                matrix[node_index[node_from]][node_index[node_to]] = value
        
        for row in matrix:
            print(row)


def main():
    graph = Graph()
    graph.add(1, 2, 1)
    graph.add(1, 3, 1)
    graph.add(2, 3, 3)
    graph.add(3, 4, 4)
    graph.add(4, 1, 5)

    graph.print_adj_list()
    graph.print_adj_matrix()


if __name__ == "__main__":
    main()
