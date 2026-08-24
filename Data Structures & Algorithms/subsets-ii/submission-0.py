from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num]+=1
        
        subset_list = []
        subset = []
        unique_nums = list(num_dict.keys())
        num_of_unique_nums = len(unique_nums)

        def generate(index):
            if index >= num_of_unique_nums:
                subset_list.append(subset.copy())
                return
            
            current_num = unique_nums[index]
            for i in range(num_dict[current_num]+1):
                subset.extend([current_num]*i)
                generate(index+1)
                for _ in range(i):
                    subset.pop()
        
        generate(0)
        return subset_list