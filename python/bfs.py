from collections import deque

class Solution:
    def bfs(self, graph, start):
        visited, queue = {start}, deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

# Example usage:
graph_data = {
    'A': ['B', 'C'], 'B': ['D', 'E'],
    'C': ['F'], 'D': [], 'E': ['F'], 'F': []
}
solver = Solution()
print(f"BFS order: {solver.bfs(graph_data, 'A')}")