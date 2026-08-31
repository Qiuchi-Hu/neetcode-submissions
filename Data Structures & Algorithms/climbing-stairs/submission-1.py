class Solution:
    def climbStairs(self, n: int) -> int:
        record = [-1]*(n+1)
        record[-1] = 1

        def find(p):
            nonlocal record
            if p > n:
                return 0
            
            if record[p] != -1:
                return record[p]
            
            record[p] = find(p+1)+find(p+2)
            return record[p]
        

        return find(0)