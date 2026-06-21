class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None
        for num in nums:
            if num == prev:
                return True
            prev = num
        
        return False
        