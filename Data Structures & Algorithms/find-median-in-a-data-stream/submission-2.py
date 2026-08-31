class MedianFinder:

    def __init__(self):
        self.total = 0
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and self.max_heap[0] > num:
            max_val = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap,max_val)

        heapq.heappush(self.min_heap,num)
        self.total +=1
        half = int(self.total/2)
        while len(self.max_heap) < half:
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, min_val)

    def findMedian(self) -> float:
        #print("="*30)
        #print("min: ", self.min_heap)
        #print("max: ", self.max_heap)
        if self.total % 2 == 0:
            return float(self.min_heap[0]+self.max_heap[0])/2
        else:
            return self.min_heap[0]
        
        