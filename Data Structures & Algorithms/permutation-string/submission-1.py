from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_len = len(s2)

        if s2_len < len(s1):
            return False

        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c]+=1
        #print(s1_freq)


        left=0
        right=0
        s2_freq = s1_freq.copy()

        while right <= s2_len:
            if sum(s2_freq.values()) == 0:
                return True
            elif right == s2_len:
                return False

            c = s2[right]
            if c not in s1_freq:
                right+=1
                left=right
                s2_freq = s1_freq.copy()
                continue

            s2_freq[c]-=1

            while s2_freq[c]<0 and left < right:
                s2_freq[s2[left]]+=1
                left+=1

            right+=1
            
            '''
            print("="*10)
            print("left: ", left)
            print("right： ", right)
            print("c: ", c)
            '''
            
        

        

