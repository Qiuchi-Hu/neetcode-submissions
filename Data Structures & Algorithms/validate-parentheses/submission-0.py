class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack)>0:
                if (c == ')' and stack[-1] == '(') or (c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '['):
                    stack.pop()
                    continue
            
            stack.append(c)
        
        if len(stack)>0:
            return False
        else:
            return True
