class Solution:
    def longestPalindrome(self, s: str) -> str:
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
            return s[0]

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

        max_len = 0
        max_start = 0
        while center_part:
            start,end = center_part.popleft()
            center = int((start+end)/2)
            d = center - start
            i = 1
            while i < d+1:
                if s[center-i] != s[center+i]:
                    break
                i += 1
            
            cur_len = 2*(i-1)+1
            if cur_len > max_len:
                max_start = center - (i-1)
                max_len = cur_len

        while part:
            start, end = part.popleft()
            if end+1-start <= max_len:
                continue
            
            for i in range(start, end+1):
                if (i - start)*2 < max_len-2:
                    continue
                if (end-i)*2 < max_len-1:
                    break
                odd_pad = True
                odd_len = 1
                even_pad = False
                even_len = 0
                odd_start = start
                even_start = start
                if i<end and s[i]==s[i+1]:
                    even_pad = True
                    even_len = 2
                
                for j in range(1,min(i-start,end-i)+1):
                    if odd_pad and s[i-j] == s[i+j]:
                        odd_len+=2
                        odd_start = i-j
                    else:
                        odd_pad = False
                    
                    if even_pad and i+j<end and s[i-j] == s[i+j+1]:
                        even_len+=2
                        even_start = i-j
                    else:
                        even_pad = False
                    

                    if not (odd_pad or even_pad):
                        break
                
                max_len = max(max_len, odd_len, even_len)
                if max_len == odd_len:
                    max_start = odd_start
                elif max_len == even_len:
                    max_start = even_start


        return s[max_start:max_start+max_len]


        

        

            