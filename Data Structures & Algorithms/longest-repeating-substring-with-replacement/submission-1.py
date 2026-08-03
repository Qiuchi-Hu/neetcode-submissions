class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        max_len = 0
        left = 0
        right = 0
        str_len = len(s)

        while right < str_len:
            c = s[right]
            if c not in freq:
                freq[c] = 1
            else:
                freq[c]+=1
            
            max_freq = max(max_freq, freq[c])
            wind_len = right - left + 1
            if wind_len - max_freq <= k:
                max_len = max(max_len,wind_len)
                #print("="*10)
                #print("wind_len: ",wind_len)
                #print("right: ",right)
                #print("left: ", left)
            else:
                while wind_len - max_freq > k and left <= right:
                    freq[s[left]]-=1
                    max_freq = max(freq.values())
                    left+=1
                    wind_len-=1
            
            right+=1
        
        return max_len
            

