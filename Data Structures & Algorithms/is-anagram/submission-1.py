class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0]*26
        a_ord = ord("a")
        for s_char, t_char in zip(s,t):
            count[ord(s_char)-a_ord]+=1
            count[ord(t_char)-a_ord]-=1
        
        for c in count:
            if c!=0:
                return False
        
        return True