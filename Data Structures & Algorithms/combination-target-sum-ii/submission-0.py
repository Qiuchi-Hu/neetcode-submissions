from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        record = defaultdict(int)
        for c in candidates:
            record[c]+=1

        unique_nums = sorted(record.keys(), reverse = True)
        combination = []
        current_comb = []
        len_unique_nums = len(unique_nums)

        def explore(index):
            current_sum = sum(current_comb)

            if current_sum == target:
                combination.append(current_comb.copy())
            elif current_sum < target:
                for i in range(index,len_unique_nums):
                    if record[unique_nums[i]]>0:
                        current_num = unique_nums[i]
                        record[current_num]-=1
                        current_comb.append(current_num)
                        explore(i)
                        current_comb.pop()
                        record[current_num]+=1
            
            return
        
        explore(0)
        return combination

