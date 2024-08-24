graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

result = []


def dfs(vertex):
    visited = [vertex]
    stack = [vertex]

    while stack:
        stack_out = stack.pop()
        result.append(stack_out)

        for adjacentVertex in graph[stack_out]:
            if adjacentVertex not in visited:
                stack.append(adjacentVertex)
                visited.append(adjacentVertex)


dfs('B')
print(result)
