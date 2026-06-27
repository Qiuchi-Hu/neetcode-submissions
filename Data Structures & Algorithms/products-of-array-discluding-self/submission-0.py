class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = int(1)
        zero_count = 0
        first_zero_index = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                total_product *= num
            else:
                zero_count+=1
                if zero_count ==1:
                    first_zero_index = i
        
        if zero_count >1:
            return [0]*len(nums)

        if zero_count == 1:
            output = [0]*len(nums)
            output[first_zero_index] = total_product
            return output

        output = []
        for i in range(len(nums)):
            output.append(int(total_product/nums[i]))
        return output