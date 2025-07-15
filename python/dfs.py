class Solution:
    def dfs(self, graph, start):
        visited = set()
        order = []

        def _dfs_util(node):
            visited.add(node)
            order.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    _dfs_util(neighbor)
        
        _dfs_util(start)
        return order

# Example usage:
graph_data = {
    'A': ['B', 'C'], 'B': ['D', 'E'],
    'C': ['F'], 'D': [], 'E': ['F'], 'F': []
}
solver = Solution()
print(f"DFS order: {solver.dfs(graph_data, 'A')}")