class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = prices[0]

        for i in range(len(prices)):
            if min_val >= prices[i]:
                min_val = prices[i]
            elif (ans < (prices[i] - min_val)):
                ans = prices[i] - min_val


        return ans