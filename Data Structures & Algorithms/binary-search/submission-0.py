class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_index = ((right - left) // 2) + left
            mid = nums[mid_index]
            if(mid == target):
                return mid_index
            elif(mid < target):
                left = mid_index + 1
            else:
                right = mid_index - 1 

        return -1