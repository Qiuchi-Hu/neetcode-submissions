from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)

            if x == y:
                continue
            heappush(stones, -(y - x))

        return -heappop(stones) if stones else 0 
