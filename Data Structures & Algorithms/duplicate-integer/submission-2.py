class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = set()
        for i in nums:
            if(i in hash_nums):
                return True
            else:
                hash_nums.add(i)

        return False