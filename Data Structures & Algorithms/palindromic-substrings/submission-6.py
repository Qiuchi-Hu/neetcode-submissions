class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        pads = 0
        for i in range(len_s):
            odd_pad = True
            pads+=1
            even_pad = False
            if i<len_s-1 and s[i]==s[i+1]:
                even_pad = True
                pads+=1
            
            for j in range(1,min(i,len_s-1-i)+1):
                if odd_pad and s[i-j] == s[i+j]:
                    pads+=1
                else:
                    odd_pad = False
                
                if even_pad and i+j<len_s-1 and s[i-j] == s[i+j+1]:
                    pads+=1
                else:
                    even_pad = False
                

                if not (odd_pad or even_pad):
                    break

        return pads


        

        

            