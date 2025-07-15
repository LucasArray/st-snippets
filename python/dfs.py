def dfs(self, graph, start):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)