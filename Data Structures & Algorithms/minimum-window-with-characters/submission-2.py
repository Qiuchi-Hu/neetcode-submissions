from collections import defaultdict
from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_substr = ""

        if len(t) > len(s):
            return shortest_substr
        
        len_shortest_substr = float("inf")

        freq_t = defaultdict(int)
        for c in t:
            freq_t[c]+=1

        freq_s = freq_t.copy()
        left = 0
        right = 0
        s_len = len(s)
        t_char_queue = deque()
        while right < s_len:
            c = s[right]
            if c in freq_t:
                freq_s[c]-=1
                t_char_queue.append(right)
                '''
                while freq_s[c]<0 and left < right:
                    if s[left] in freq_s:
                        freq_s[s[left]]+=1
                        t_char_queue.popleft()
                    left = t_char_queue[0]
                '''
                print("="*10)
                print("c: ",c)
                print("left: ",left)
                print("right: ", right)
                print("freq_s: ", freq_s)
                

                if t_char_queue:
                    left = t_char_queue[0]
                while sum(max(0,val) for val in freq_s.values()) == 0 and left <= right:
                    print("-"*10)
                    print("left: ",left)
                    current_len = right-left+1
                    if current_len < len_shortest_substr:
                        shortest_substr = s[left:right+1]
                        len_shortest_substr = current_len
                        print("shortest_substr: ", shortest_substr)
                    freq_s[s[left]]+=1
                    t_char_queue.popleft()
                    if t_char_queue:
                        left = t_char_queue[0]
            
            right +=1
        
        return shortest_substr

