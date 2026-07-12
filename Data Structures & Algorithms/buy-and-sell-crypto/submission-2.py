# The most succint answer... I feel like it should be worse as 
# It always completes calculations which are not always relevant.
# However, for the sake of keeping things succint and quick (which matters in interviews)
# This may be better...

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP