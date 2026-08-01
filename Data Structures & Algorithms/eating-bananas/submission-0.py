def canFinish(piles,h, k):
    total_h = 0

    for p in piles:
        total_h += math.ceil(p/k)

    return total_h <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right_k = max(piles)
        left_k = 1
        last_can_mid = 0

        while left_k <= right_k:
            mid_k = (left_k+right_k)//2
            if canFinish(piles, h, mid_k):
                last_can_mid = mid_k
                right_k = mid_k-1
            else:
                left_k = mid_k+1
            
        return last_can_mid
            
