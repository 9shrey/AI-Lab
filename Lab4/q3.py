def tsp_bfs(graph, start):
    queue = [(start, [start], 0)]  # (current_node, path, cost)
    min_cost = float('inf')
    min_path = []

    while queue:
        current_node, path, cost = queue.pop(0)

        if len(path) == len(graph) and graph[current_node][start] != 0:
            # If all nodes are visited and there is a path back to the start node
            cost += graph[current_node][start]
            if cost < min_cost:
                min_cost = cost
                min_path = path + [start]

        for neighbor in graph[current_node]:
            if neighbor not in path and graph[current_node][neighbor] != 0:
                # Add unvisited neighbors to the queue
                queue.append((neighbor, path + [neighbor], cost + graph[current_node][neighbor]))

    return min_path, min_cost
def main():
    graph = {
        'A': {'B': 2, 'C': 3, 'D': 1},
        'B': {'A': 2, 'C': 4, 'D': 2},
        'C': {'A': 3, 'B': 4, 'D': 3},
        'D': {'A': 1, 'B': 2, 'C': 3}
    }
    start_node = 'A'
    min_path, min_cost = tsp_bfs(graph, start_node)
    print("Minimum path:", min_path)
    print("Minimum cost:", min_cost)

if __name__ == "__main__":
    main()
