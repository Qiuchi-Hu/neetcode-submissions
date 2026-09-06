class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 4:
            return max(nums)

        # with nums[0], without nums[0]
        nums[0] = (nums[0],0)
        nums[1] = (nums[1],nums[1])
        nums[2] = (nums[2]+nums[0][0],nums[2])

        for i in range(3, len_nums):
            with_0 = max(nums[i-2][0],nums[i-3][0])
            without_0 = max(nums[i-2][1],nums[i-3][1])
            nums[i] = (nums[i]+with_0,nums[i]+without_0)
        
        #print(nums)
        return max(nums[-3][0],max(nums[-2]),nums[-1][1])

