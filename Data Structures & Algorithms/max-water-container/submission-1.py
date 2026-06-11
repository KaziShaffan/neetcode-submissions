class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            gap = right - left

            if(left_height > right_height):
                current = right_height * gap
                right -= 1
            else:
                current = left_height * gap
                left += 1
 
            best = max(current,best)

        return best
            

            
            