class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #if matrix[0][0] >target or matrix[-1][-1] < target:
            #return False

        left_r = 0
        right_r = len(matrix) - 1
        mid = 0
        mid_r = 0

        while left_r <= right_r:
            mid_r = (left_r + right_r) // 2
            mid = matrix[mid_r][0]

            if mid == target:
                return True
            elif mid < target:
                left_r = mid_r + 1
            else:
                right_r = mid_r - 1
        
        if mid > target:
            mid_r -=1
        
        left_c = 1
        right_c = len(matrix[mid_r])-1

        while left_c <= right_c:
            mid_c = (left_c+right_c)//2
            mid = matrix[mid_r][mid_c]

            if mid == target:
                return True
            elif mid < target:
                left_c = mid_c+1
            else:
                right_c = mid_c -1
        
        return False


