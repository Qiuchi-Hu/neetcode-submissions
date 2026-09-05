class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return [a,b]
            
            parent[root_b] = root_a