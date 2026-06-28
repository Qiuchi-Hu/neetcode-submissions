class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack:
                top = stack[-1]
                if top[1] < t:
                    result[top[0]] = i - top[0]
                    stack.pop()
                else:
                    break
            
            stack.append([i,t])
        
        return result
            
