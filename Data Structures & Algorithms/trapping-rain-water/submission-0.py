class Solution:
    def trap(self, height: List[int]) -> int:
        if(not height):
            return 0


        left = 0
        right = len(height) - 1
        ans = 0

        left_h = height[left]
        right_h = height[right]

        while left < right:
            

            if(left_h < right_h):
                left += 1
                left_h = max(left_h, height[left])
                ans += left_h - height[left]
            else:
                right -= 1
                right_h = max(right_h, height[right])
                ans += right_h - height[right]



        return ans

            

                

