class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        right = max(piles)
        left = 1
        
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            for i in piles:
               total_hours += math.ceil(i / mid)

            if(total_hours <= h):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
            

            
        
            

            
