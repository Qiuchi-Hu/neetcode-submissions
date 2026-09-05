class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 0
        count = 0
        left = 0
        right = 1
        max_right = 2

        while True:
            for i in range(left, right):
                if nums[i]+i>=len_nums-1:
                    return count+1
                max_right = max(max_right,nums[i]+i+1)
            count+=1
            left = right
            right = max_right
                

                
                
            
