# O(n) possible definitely, O(1) space possi
# 10 (0), 1 (0), 5 (4), 6 (5), 7 (6), 1 (6)
# 10, 8, 9, 10, 10, 3, 9, 10
# 0, 0, 1, 1, 1, 1, 6, 6

# 8, 8, 3, 8, 2, 8, 11
# 0, 0, 0, 5, 5, 6, 9

# initialise best as 0 and track max and min. Max starts at Min starts at the first entry
# As you iterate, update max and min. If min changes, change max
# If max changes, then check for increase in best
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi = prices[0], prices[0]
        best = 0

        for price in prices:
            if price < mini:
                mini = price
                maxi = price
                
            elif price > maxi:
                maxi = price
                best = max(best, maxi - mini)

        return best