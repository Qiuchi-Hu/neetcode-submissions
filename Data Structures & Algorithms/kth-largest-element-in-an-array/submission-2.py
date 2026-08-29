class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)/2 >= k:
            heapq.heapify_max(nums)
            for _ in range(k-1):
                heapq.heappop_max(nums)
        else:
            heapq.heapify(nums)
            k = len(nums)-k
            for _ in range(k):
                heapq.heappop(nums)
        
        return nums[0]
    
        