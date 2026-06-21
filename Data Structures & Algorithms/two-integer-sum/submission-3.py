class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        sorted_nums = sorted(nums)
        
        i=0
        j = len_nums -1
        target_i = None
        target_j = None
        while(i<j):
            if sorted_nums[i] + sorted_nums[j] == target:
                target_i = sorted_nums[i]
                target_j = sorted_nums[j]
                break
            elif sorted_nums[i] + sorted_nums[j] > target:
                j-=1
            else: 
                i+=1

        print("target i is: ", target_i)
        print("target j is: ", target_j)
        return_index = []
        for k in range(len(nums)):
            if target_i is not None and nums[k]==target_i:
                return_index.append(k)
                target_i = None
            elif target_j is not None and nums[k]==target_j:
                return_index.append(k)
                target_j = None
            elif target_i is None and target_j is None:
                break
        
        return return_index
            
        