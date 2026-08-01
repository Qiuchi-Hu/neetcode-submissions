class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            if left == right:
                return nums[left]
            if nums[left] > nums[left+1]:
                return nums[left+1]
            left +=1
            if nums[right] < nums[right-1]:
                return nums[right]
            right -=1


        