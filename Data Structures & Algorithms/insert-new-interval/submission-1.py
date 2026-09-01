class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        output_list = []
        inserted = False
        for start,end in intervals:
            if end < new_start:
                output_list.append([start,end])
                continue
            if start > new_end:
                if not inserted:
                    output_list.append([new_start,new_end])
                    inserted = True
                output_list.append([start,end])
                continue
            
            new_start = min(start,new_start)
            new_end = max(end, new_end)
        
        if not inserted:
            output_list.append([new_start,new_end])
        return output_list

                