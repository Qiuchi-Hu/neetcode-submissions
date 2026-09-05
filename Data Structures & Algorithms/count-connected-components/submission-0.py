class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for a, b in edges:
            if not a in graph:
                graph[a] = []
            if not b in graph:
                graph[b] = []
            
            graph[a].append(b)
            graph[b].append(a)
        
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
            if len(visited) == n:
                break
        
        return count