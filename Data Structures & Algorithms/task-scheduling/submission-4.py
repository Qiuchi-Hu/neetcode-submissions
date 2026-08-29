class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_count = {}
        for task in tasks:
            if task in frequency_count:
                frequency_count[task]+=1
            else:
                frequency_count[task]=1
        
        queue = []
        frequency_heap = []
        for task, freq in frequency_count.items():
            heapq.heappush_max(frequency_heap, (freq, task))

        second = 0
        while True:
            #print(frequency_heap)
            pop_times = min(len(frequency_heap),n+1)
            for _ in range(pop_times):
                freq, task = heapq.heappop_max(frequency_heap)
                freq-=1
                if freq:
                    queue.append((freq,task))
            if not queue and not frequency_heap:
                return second+pop_times
            if pop_times > n+1:
                second+=pop_times
            else:
                second = second+n+1
            
            for item in queue:
                heapq.heappush_max(frequency_heap,item)
            queue = []
        
        return -1


