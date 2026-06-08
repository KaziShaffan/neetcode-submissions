class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        
        
        ans = 0
        k = 0
        for i in range(len(nums)):
            if(nums[i] - 1 in hash_nums):
                continue
            else:
                k = nums[i]
                count = 1
                while True:
                    if((k + 1) in hash_nums):
                        k += 1
                        count += 1
                    else:
                        if(count > ans):
                            ans = count
                        break
                    
        print(ans)
        return ans

