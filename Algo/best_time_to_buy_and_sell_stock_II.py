"""

122. Best Time to Buy and Sell Stock II (Easy)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i]-prices[i-1])
        return max_profit

if __name__=="__main__":
    sol = Solution()
    p1 = [7, 1, 5, 3, 6, 5]
    print(sol.maxProfit(p1))