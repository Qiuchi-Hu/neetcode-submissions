class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        if edges:
            parents = list(range(n))

            def find(x):
                while x != parents[x]:
                    x = parents[x]
                return x
            
            for o,e in edges:
                root_o = find(o)
                root_e = find(e)

                if root_o == root_e:
                    return False
                
                parents[root_e] = root_o
            
        return True