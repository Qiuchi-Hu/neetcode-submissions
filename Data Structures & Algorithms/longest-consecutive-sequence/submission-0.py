from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for num in num_set:
            if num-1 not in num_set:
                current_seq = 1
                next = num+1
                while next in num_set:
                    current_seq +=1
                    next+=1
                if current_seq > max_seq:
                    max_seq = current_seq
        
        return max_seq

