# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_revenue = 0
        buy_price = prices[0]

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            max_revenue = max(max_revenue, p - buy_price)

        return max_revenue


solution = Solution()

max_profit = solution.maxProfit([3,2,6,5,0,3])

