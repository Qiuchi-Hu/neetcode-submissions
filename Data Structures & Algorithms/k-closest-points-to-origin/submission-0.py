class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            heapq.heappush_max(max_heap,(math.sqrt(x**2+y**2),[x,y]))
            if len(max_heap)> k:
                heapq.heappop_max(max_heap)
        
        closest_nodes = []
        for _ in range(k):
            _, coordinate = heapq.heappop_max(max_heap)
            closest_nodes.append(coordinate)
        
        return closest_nodes