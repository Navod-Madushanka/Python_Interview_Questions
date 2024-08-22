def dijkstra(start_node, graph):
    unvisited = {}
    visited = {}

    # Initialize all nodes as unvisited with infinite distance
    for node in graph:
        unvisited[node] = float('inf')

    # Distance to the start node is zero
    current = start_node
    unvisited[current] = 0

    while unvisited:
        # Select the unvisited node with the smallest distance
        current, currentDistance = min(unvisited.items(), key=lambda x: x[1])

        # Iterate over the neighbors of the current node
        for neighbor, distance in graph[current].items():
            if neighbor not in unvisited:
                continue

            newDistance = currentDistance + distance

            # Update the distance for the neighbor if a shorter path is found
            if newDistance < unvisited[neighbor]:
                unvisited[neighbor] = newDistance

        # Mark the current node as visited
        visited[current] = currentDistance
        del unvisited[current]

    return visited


start_node = 'A'

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 35, 'E': 10},
    'C': {'A': 10, 'D': 10, 'E': 30},
    'D': {'B': 35, 'C': 20, 'E': 10},
    'E': {'B': 10, 'D': 10, 'C': 30}
}

result = dijkstra(start_node, graph)
print(result)
