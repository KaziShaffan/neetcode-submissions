class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        ans = []
        nums.sort()

        for i,current_ind1 in enumerate(nums):
            if i > 0 and current_ind1 == nums[i-1]:
                continue
            else:
                left = i+1
                right = len(nums) -1
                target = 0 - current_ind1
                while left < right:
                    if(target < nums[left] + nums[right]):
                        right -= 1
                    elif(target > nums[left] + nums[right]):
                        left += 1
                    else:
                        ans.append([current_ind1,nums[left],nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        
        

        


        return ans
        
        