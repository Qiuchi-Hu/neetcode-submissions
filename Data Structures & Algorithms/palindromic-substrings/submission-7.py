class Solution:
    def countSubstrings(self, s: str) -> int:
        s2 = '#'
        for i in s:
            s2 = s2 + i + '#'
        p = [0]*len(s2)
        center = 0
        right = 0
        for i in range(len(s2)):
            p[i] = min(right-i,p[center+right-i]) if i<right else 0
            while (i + p[i] + 1 < len(s2) and i - p[i] - 1 >= 0
                       and s2[i + p[i] + 1] == s2[i - p[i] - 1]):
                    p[i] += 1
            if i + p[i] > right:
                    center, right = i - p[i], i + p[i]
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res