class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))
        pairs.sort(reverse=True)
        fleet = 0
        longest_time = -float("inf")

        for p, s in pairs:
            t = (target - p)/s

            if t > longest_time:
                fleet +=1
                longest_time = t
        
        return fleet