class Solution:
    def countSubstrings(self, s: str) -> int:
        s2 = '#'
        for i in s:
            s2 = s2 + i + '#'
        p = [0]*len(s2)
        
        # s2 will follow the pattern
        # "#a#b#c...#e#f#"
        # 这个pattern把odd palindrome (center是字符a-z）和even palindrome (center是#)统一成odd palindrome来处理

        # 在一个已经确认的padlindrome substring里
        # (left)#a#b#c#b#a#b#c#b#a#(right)
        # 左边的c和右边的c在padlindrome区间内周围的环境都是一致的
        # 如果以左边c为中心的padlindrome半径是2（在区间内），那么以右边c为中心的padlindrome也可以推断至少有2；超出2的部分，即超出区间right边界的部分还需要再推断
        left = 0
        right = 0
        len_s2 = len(s2)
        for i in range(len_s2):
            p[i] = 0 if i >= right else min(right-i,p[left+right-i])
            while(i+p[i]+1<len_s2 and i-p[i]-1>=0 and s2[i+p[i]+1] == s2[i-p[i]-1]):
                p[i]+=1
            if i+p[i]>right:
                left,right = i-p[i], i+p[i]
        
        # 当s2[i]是字符时，p[i]至少是1，因为s2的format保证#a#(字符被#包围)
        res = 0
        for i in p:
            res += (i+1)//2
        
        return res