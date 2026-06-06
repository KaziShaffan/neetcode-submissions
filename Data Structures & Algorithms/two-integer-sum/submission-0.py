class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if(diff not in hash_nums.keys()):
                hash_nums[nums[i]] = i 
                print(hash_nums)
            else:
                return [hash_nums[diff], i]

        return [0,0]   
        
        