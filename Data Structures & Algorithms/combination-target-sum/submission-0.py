class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums,reverse=True)
        #print(nums)
        combination = []
        current_com = []
        num_of_nums = len(nums)

        def explore(index):
            #nonlocal combination, current_com,num_of_nums
            current_sum = sum(current_com)
            
            #print(current_com)
            
            if current_sum == target:
                combination.append(current_com.copy())
            elif current_sum < target:
                for i in range(index, num_of_nums):
                    current_com.append(nums[i])
                    explore(i)
                    current_com.pop()

            return
        
        explore(0)
        return combination