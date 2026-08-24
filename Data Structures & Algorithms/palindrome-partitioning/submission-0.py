from collections import defaultdict
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        list_of_palindromes = []
        substring = []
        num_of_chars = len(s)

        def isPalindrome(string):
            left = 0
            right = len(string)-1

            while left < right:
                if string[left]!=string[right]:
                    return False
                
                left+=1
                right-=1
            
            return True


        def explore(index):
            for i in range(index, num_of_chars):
                current_split = s[index:i+1]
                if isPalindrome(current_split):
                    substring.append(current_split)
                    if i == num_of_chars-1:
                        list_of_palindromes.append(substring.copy())
                    else:
                        explore(i+1)
                    substring.pop()
            
        explore(0)
        return list_of_palindromes


            
                


            