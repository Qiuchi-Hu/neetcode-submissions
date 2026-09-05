class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        if len_nums <2:
            return True
        
        for i in range(len_nums-2,-1,-1):
            if len_nums -1 - i <= nums[i]:
                if self.canJump(nums[:i+1]):
                    return True
        
        return False