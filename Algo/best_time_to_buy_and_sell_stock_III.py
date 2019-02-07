"""

123. Best Time to Buy and Sell Stock III (Hard)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


dp[transaction_id][day_id] = max(dp[transaction_id-1][day_id],
      dp[transaction_id-1][day_0~day_id] + prices[day_id]- prices[day_0~day_id])

On ith day, either no trasaction, or one more transaction based on all possible previous transactions

bETTER SOLUTION
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/213474/DP-Java-Solution-for-k-transactions

Algorithmic notes

P	1	2	3	4	5	6	7	8	9	10		
	1	2	4	2	5	7	2	4	9	0		
0	0	0	0	0	0	0	0	0	0	0		
1	0	1	3	3	4	6	6	6	8	8		
2	0	2	3	3	6	8	8	8	13	13		
												
												
												
												
		1	2	3	4	5	6	7	8	9	10
											
	1	"-INF"	0-1	0-1	0-1	0-1	0-1	0-1	0-1	0-1	0-1
	2			0-2	0-2	0-2	0-2	0-2	0-2	0-2	0-2
	3				0-4	0-4	0-4	0-4	0-4	0-4	0-4
	4					0-2	0-2	0-2	0-2	0-2	0-2
	5						0-5	0-5	0-5	0-5	0-5
	6							0-7	0-7	0-7	0-7
	7								0-2	0-2	0-2
	8									0-4	0-4
	9										0-9
MAX	10	"-INF"	-1	-1	-1	-1	-1	-1	-1	-1	-1
TRADE		(1,1)	(1,2)	(1,3)	(1,3)	(1,5)	(1,6)	(1,6)	(1,6)	(1,9)	(1,9)
											
											
		1	2	3	4	5	6	7	8	9	10
											
	1	"-INF"	0-1	0-1	0-1	0-1	0-1	0-1	0-1	0-1	0-1
	2			1-2	1-2	1-2	1-2	1-2	1-2	1-2	1-2
	3				3-4	3-4	3-4	3-4	3-4	3-4	3-4
	4					3-2	3-2	3-2	3-2	3-2	3-2
	5						4-5	4-5	4-5	4-5	4-5
	6							6-7	6-7	6-7	6-7
	7								6-2	6-2	6-2
	8									6-4	6-4
	9										8-9
MAX	10	"-INF"	-1	-1	-1	1	1	1	4	4	4
TRADE		(1,1)	(1,2)	(1,3)	(1,3)	(4,5)	(4,6)	(4,6)	(7,8)	(7,9)	(7,9)


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

    def maxProfit(self, prices: 'List[int]') -> 'int':
        """
            TLE

        """
        if len(prices) <= 1:
            return 0

        MAX_NUM_TRANSACTIONS = 2
        n = len(prices)
        dp = [[0 for _ in range(n + 1)] for _ in range(1 + MAX_NUM_TRANSACTIONS)]
        for i in range(1, n + 1):
            for t in range(1, MAX_NUM_TRANSACTIONS + 1):
                for j in range(1, i + 1):
                    dp[t][i] = max(dp[t][i], dp[t][i-1], dp[t - 1][i], dp[t - 1][j] + prices[i-1] - prices[j-1])
        return dp[MAX_NUM_TRANSACTIONS][n]


    def maxProfit_Ktrade(self, k, prices):
        '''

        Find the maximum profit with K trades

        Dynamic programming
        Time-complexity: O(kn)

        :param prices: a list of stock prices
        :return: the trades and maximum profit up to each day
        '''


        profit = [[0 for i in range(len(prices))] for j in range(k+1)]  # profit[k][i] is the maximum profit at day i with k trades
        m = [[0 for i in range(len(prices))] for j in range(k)]    # max{p(t-1, j) - prices(j)} for j in [1, i-1]
        trades = [[None for i in range(len(prices))] for j in range(k)]

        # initialization
        for t in range(k):
            m[t][0] = -float("inf")
            trades[t][0] = (1,1)


        # dp
        for t in range(1, k+1):    # transactions
            for i in range(2, len(prices)+1):

                prev = None
                if m[t-1][(i-1)-1] >= profit[t-1][(i-1)-1] - prices[(i-1)-1]:
                    m[t-1][i-1] = m[t-1][(i-1)-1]
                    prev = (i-2,i)
                else:
                    m[t-1][i-1] = profit[t-1][(i-1)-1] - prices[(i-1)-1]
                    prev = (i-1,i)         # trade between last day and today

                if profit[t][i-2] >= m[t-1][i-1]+prices[i-1]:
                    trades[t-1][i-1] = trades[t-1][i-2]     # no trades; use the previous trade
                    profit[t][i-1] = profit[t][i-2]
                else:
                    trades[t-1][i-1] = prev
                    profit[t][i-1] = m[t-1][i-1]+prices[i-1]

        return profit, trades




if __name__=='__main__':

    sol = Solution()

    cases = [

        (sol.maxProfit, ([3,3,5,0,0,3,1,4],), 6),
        (sol.maxProfit, ([6,1,3,2,4,7],), 7),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))