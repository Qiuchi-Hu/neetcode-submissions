class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 0
        current_sum = 0
        max_sum = -float("inf")
        len_nums = len(nums)

        while right < len_nums:
            current_sum += nums[right]
            max_sum = max(current_sum,max_sum)
            current_sum = max(current_sum,0)
            right +=1
        
        return max_sum
