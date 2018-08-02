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


    def maxProfit_OneTrade(self, prices):
        min_price, max_profit = float("inf"), 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p - min_price, max_profit)
        return max_profit


    def maxProfit_Ktrade(self, k, prices):
        '''

        Find the maximum profit with K trades

        Dynamic programming
        Time-complexity: O(kn)

        :param prices: a list of stock prices
        :return:
        '''


        profit = [[0 for i in range(len(prices))] for j in range(k+1)]  # profit[k][i] is the maximum profit at day i with k trades
        m = [[0 for i in range(len(prices))] for j in range(k+1)]    # max{p(t-1, j) - prices(j)} for j in [1, i-1]

        # initialization
        # for j in range(1, len(prices)+1):
        #     m[0][j] = profit[0][j] - prices[j-1]

        # dp
        for k in range(1, k+1):
            for i in range(1,len(prices)+1):
                if i == 1:  # day 1
                    m[k-1][i-1] = profit[k-1][i-1] - prices[i-1]
                else:
                    m[k-1][i-1] = max(m[k-1][i-2], profit[k - 1][i - 1] - prices[i - 1])
                    profit[k][i-1] = max(profit[k][i-2], m[k-1][i-1]+prices[i-1])


        return profit



if __name__=="__main__":
    sol = Solution()
    # p = [7, 1, 5, 3, 6, 5]
    # p = [1,2,4]
    # p = [2,1,2,0,1]
    p = [1,2,4,2,5,7,2,4,9,0]
    print(sol.maxProfit_Ktrade(2, p))
    # print(sol.maxProfit_Slow(p))