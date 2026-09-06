class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        
        max_len = 1
        start = 0

        for i in range(len_s-1):
            odd_pad = True
            even_pad = False
            even_len = 0
            if s[i] == s[i+1]:
                even_pad = True
                even_len = 2
            
            odd_len = 1
            odd_start = i
            even_start = i
            for j in range(1,min(i+1,len_s-i)):
                if s[i-j] != s[i+j]:
                    odd_pad = False
                elif odd_pad:
                    odd_len+=2
                    odd_start = i-j
                    
                if i+j+1 < len_s:
                    if s[i-j] != s[i+j+1]:
                        even_pad = False
                    elif even_pad:
                        even_len+=2
                        even_start = i-j
                else:
                    even_pad = False
                
                if not odd_pad and not even_pad:
                    break

            max_len = max(max_len, odd_len, even_len)
            if max_len == odd_len:
                start = odd_start
            elif max_len == even_len:
                start = even_start
            
            if max_len - 1 > (len_s - i - 2)*2:
                break
            

        
        #print(start)
        return s[start:start+max_len]

            
            