class Solution:
    def countSubstrings(self, s: str) -> int:
        count = {}
        len_s = len(s)

        for i,ch in enumerate(s):
            if ch not in count:
                count[ch] = deque()
            count[ch].append(i)
        
        singleton = []
        for li in count.values():
            if len(li) == 1:
                singleton.append(li[0])

        
        if len(singleton) == len_s:
            return len_s

        singleton = [-1]+singleton
        
        singleton.sort()
        singleton.append(len_s)
        part = deque()
        center_part = deque()
        prev_distance = singleton[1]

        for i in range(1, len(singleton)-1):
            sep_prev = singleton[i-1]
            sep_cur = singleton[i]
            sep_next = singleton[i+1]
            cur_distance = sep_next - sep_cur -1 
            if prev_distance:
                part.append((sep_prev+1, sep_cur-1))
            distance = min(cur_distance, prev_distance)
            center_part.append((sep_cur - distance, sep_cur+distance))
            
            prev_distance = cur_distance
        
        if prev_distance:
            part.append((singleton[-2]+1,singleton[-1]-1))

        pads = []
        while center_part:
            start,end = center_part.popleft()
            center = int((start+end)/2)
            d = center - start
            pads.append(s[d])
            for i in range(1,d+1):
                if s[center-i] == s[center+i]:
                    pads.append(s[center-i:center+i+1])
                else:
                    break
        
        print(pads)
        while part:
            start, end = part.popleft()
            for i in range(start, end+1):
                odd_pad = True
                pads.append(s[i])
                even_pad = False
                if i<end and s[i]==s[i+1]:
                    even_pad = True
                    pads.append(s[i:i+2])
                
                for j in range(1,min(i-start,end-i)+1):
                    if odd_pad and s[i-j] == s[i+j]:
                        pads.append(s[i-j:i+j+1])
                    else:
                        odd_pad = False
                    
                    if even_pad and i+j<end and s[i-j] == s[i+j+1]:
                        pads.append(s[i-j:i+j+2])
                    else:
                        even_pad = False
                    

                    if not (odd_pad or even_pad):
                        break

        return len(pads)


        

        

            