class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_dict={}
        start_index = 0
        max_length = 0

        for i,c in enumerate(s):
            prev_c = start_index - 1
            #print("i: "+str(i)+" c: "+c)
            if c in c_dict:
                prev_c = c_dict[c]
            c_dict[c] = i
            if prev_c >= start_index:
                #print("max length: ",max_length)
                #print("start_index: ", start_index)
                #print("i: ",i)
                max_length=max(max_length,i-start_index)
                start_index=prev_c+1

        return max(max_length, len(s)-start_index)
            
            

        