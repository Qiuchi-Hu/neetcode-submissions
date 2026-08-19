import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        len_nums = len(nums)
        index = 0
        
        for _ in range(k):
            if index >= len_nums:
                current_max, i = heapq.heappop(max_heap)
                return [-current_max]
            
            heapq.heappush(max_heap,[-nums[index],index])
            index+=1
        
        max_nums = [-max_heap[0][0]]
        #print(max_nums)
        while index < len_nums:
            heapq.heappush(max_heap,[-nums[index],index])
            #print(max_heap)
            while max_heap[0][1]<=index-k:
                heapq.heappop(max_heap)
            max_nums.append(-max_heap[0][0])
            index+=1
        
        return max_nums




