class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1_sell = 0
        dp1_buy = 0
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            temp1 = dp1_sell
            temp2 = dp1_buy
            dp1_sell = max(dp1_sell, dp2_buy + prices[i])
            dp1_buy = max(dp1_buy, temp1 - prices[i])
            dp2_buy = temp2

        return dp1_buy

