class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalpha() or c.isdigit())
        print(s)
        left = 0
        right = len(s)-1

        while left<right:
            print(s[left])
            print(s[right])
            if s[left] != s[right]:
                print(s[left])
                print(s[right])
                return False
            
            left +=1
            right -=1
        
        return True