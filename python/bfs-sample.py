from collections import deque

# BFS using a queue on a graph represented as an adjacency list

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
