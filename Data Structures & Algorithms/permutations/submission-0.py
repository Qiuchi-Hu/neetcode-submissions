class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        current = []
        num_of_nums = len(nums)

        def explore(current_list):
            if len(current_list) == num_of_nums:
                permutation.append(current_list.copy())
                return
            
            for num in nums:
                if num in current_list:
                    continue
                
                current_list.append(num)
                explore(current_list)
                current_list.pop()
        
        explore(current)
        return permutation