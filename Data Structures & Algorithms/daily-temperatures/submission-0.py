class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i,k in enumerate(temperatures):
            while stack and stack[-1][1] < k:
                stk_i, _ = stack.pop()
                ans[stk_i] = i - stk_i


            stack.append((i, k))

        return ans