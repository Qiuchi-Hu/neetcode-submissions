class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        current = nums[0]
        subsequent = self.subsets(nums[1:])

        new_subsets = []

        #append will change the original list directly and return None
        for sub in subsequent:
            new_subsets.append(sub + [current])

        return subsequent + new_subsets