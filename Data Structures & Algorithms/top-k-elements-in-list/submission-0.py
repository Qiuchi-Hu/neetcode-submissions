class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1

        bucket = [[] for _ in range(len(nums)+1)]

        for num, c in count.items():
            bucket[c].append(num)

        result = []

        for i in range(len(bucket)-1, 0, -1):
            result.extend(bucket[i])
            if len(result) >=k:
                return result[:k]

        
        