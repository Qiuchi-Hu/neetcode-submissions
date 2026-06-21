class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for s_char, c_char in zip(sorted_s, sorted_t):
            if s_char != c_char:
                return False
        return True