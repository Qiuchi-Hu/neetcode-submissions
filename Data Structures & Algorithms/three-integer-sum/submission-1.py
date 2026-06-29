class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        #print(nums)
        for i in range(len(nums)-2):
            target = -nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:
                #print("left:",nums[left],"right:",nums[right],"target:",target)
                sum_result = nums[left]+nums[right]
                if sum_result == target:
                    result.add((-target,nums[left],nums[right]))
                    left +=1
                elif sum_result < target:
                    left +=1
                else:
                    right -=1
            
        return list(result)
