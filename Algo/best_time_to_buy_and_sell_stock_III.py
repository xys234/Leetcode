"""

123. Best Time to Buy and Sell Stock III (Hard)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""


class Solution:
    def maxProfit_Slow(self, prices):
        max_profit = 0
        profit_1 = 0
        profit_2 = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit_1 = prices[j] - prices[i]
                if len(prices) - 1 - j >= 2:
                    profit_2 = self.maxProfit_OneTrade(prices[j:])
                else:
                    profit_2 = 0
                max_profit = max(max_profit, profit_1+profit_2)
        return max_profit

    def maxProfit_1Pass(self, prices):
        profit_1 = profit_2 = 0
        i = 0
        while i < len(prices):
            j = i+1
            while j < len(prices) and prices[j] <= prices[i]:
                j += 1
            # if i >= len(prices) or j >= len(prices):
            #     break
            change = prices[j] - prices[i]
            if change > profit_1:
                profit_2 = profit_1
                profit_1 = change
            elif change < profit_1 and change > profit_2:
                profit_2 = change
            i, j = j, j+1
        return profit_1 + profit_2

    def maxProfit(self, prices):
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2    = max(hold2,    release1 - i)
            release1 = max(release1, hold1 + i)
            hold1    = max(hold1,    -i);
        return release2


    def maxProfit_OneTrade(self, prices):
        min_price, max_profit = float("inf"), 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p - min_price, max_profit)
        return max_profit



if __name__=="__main__":
    sol = Solution()
    # p = [7, 1, 5, 3, 6, 5]
    # p = [1,2,4]
    # p = [2,1,2,0,1]
    p = [1,2,4,2,5,7,2,4,9,0]
    print(sol.maxProfit(p))
    # print(sol.maxProfit_Slow(p))