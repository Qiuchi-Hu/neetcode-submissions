class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        pads = []
        for i in range(len_s):
            odd_pad = True
            pads.append(s[i])
            even_pad = False
            if i<len_s-1 and s[i]==s[i+1]:
                even_pad = True
                pads.append(s[i:i+2])
            
            for j in range(1,min(i,len_s-1-i)+1):
                if odd_pad and s[i-j] == s[i+j]:
                    pads.append(s[i-j:i+j+1])
                else:
                    odd_pad = False
                
                if even_pad and i+j<len_s-1 and s[i-j] == s[i+j+1]:
                    pads.append(s[i-j:i+j+2])
                else:
                    even_pad = False
                

                if not (odd_pad or even_pad):
                    break

        return len(pads)


        

        

            