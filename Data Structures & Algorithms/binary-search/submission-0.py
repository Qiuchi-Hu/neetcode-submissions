class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2
            mid_num = nums[mid]

            if mid_num == target:
                return mid
            elif mid_num > target:
                right = mid -1
            else:
                left = mid +1
        
        return -1