class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_index = ((right - left) // 2) + left
            if(nums[mid_index] == target):
                return mid_index
            elif(nums[mid_index] < target):
                left = mid_index + 1
            else:
                right = mid_index - 1 

        return -1