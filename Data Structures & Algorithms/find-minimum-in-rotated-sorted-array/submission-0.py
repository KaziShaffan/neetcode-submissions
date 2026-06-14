class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_set = set(nums)

        smallest = min(nums_set)

        return smallest