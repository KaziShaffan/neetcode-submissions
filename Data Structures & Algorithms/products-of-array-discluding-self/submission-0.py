class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if(len(nums) == 0 or len(nums) == 1):
            return []

        prefix_nums = [1]*(len(nums))
        prefix = 1
     

        for i in range(len(nums)):
            
            prefix *= nums[i]
            prefix_nums[i] = prefix


        postfix_nums = [1] * len(nums)
        postfix = 1

        for k in reversed(range(len(nums))):
            postfix *= nums[k]
            postfix_nums[k] = postfix
            

        ans = [1] * len(nums)

        for j in range(len(nums)):
            if(j == 0):
                ans[j] = 1 * postfix_nums[j+1]
            elif(j == len(nums)-1):
                ans[j] = 1 * prefix_nums[j-1]
            else:
                ans[j] = prefix_nums[j-1] * postfix_nums[j+1]


        return ans
            
            
