class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # every bar is looking for the furthest bar that is higher than itself
        left = 0
        right = len(heights)-1
        max_area = -float("inf")

        while left < right:
            left_bar = heights[left]
            right_bar = heights[right]

            if left_bar < right_bar:
                max_area = max(max_area, left_bar*(right-left))
                left+=1
            else:
                max_area = max(max_area, right_bar*(right-left))
                right-=1
        
        return max_area