"""

188.

Hard

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

History:
2019.07.12

"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        profits = [[0 for _ in range(days)] for _ in range(k+1)]

        if k > 2*days:
            return self.helper(prices)

        if k == 0 or days == 0:
            return 0

        for j in range(1, k+1):
            max_diff = 0
            for d in range(1, days):
                if d == 1:
                    max_diff = profits[j - 1][0] - prices[0]
                else:
                    max_diff = max(max_diff, profits[j - 1][d - 1] - prices[d-1])
                profits[j][d] = max(profits[j][d-1], max_diff+prices[d])
        return profits[-1][-1]

    def helper(self, prices):
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += prices[i + 1] - prices[i]

        return res

    def maxProfit_solution(self, k: int, prices: List[int]) -> int:
        if k >= int(len(prices) / 2):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        if len(prices) == 0 or k == 0:
            return 0
        buy = [-prices[0] for i in range(k)]
        sell = [0 for i in range(k)]
        for p in prices:
            for i in range(k):
                if i - 1 >= 0:
                    buy[i] = max(buy[i], sell[i - 1] - p)
                else:
                    buy[i] = max(buy[i], 0 - p)
                sell[i] = max(sell[i], buy[i] + p)
        return sell[-1]

    def maxProfit_dp(self, k: int, prices: List[int]) -> int:
        if not k or not prices:
            return 0

        if k >= len(prices) / 2:
            return self.helper(prices)

        local = [[0 for _ in range(len(prices))] for _ in range(k + 1)]
        dp = [[0 for _ in range(len(prices))] for _ in range(k + 1)]

        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                local[i][j] = max(dp[i - 1][j - 1], local[i][j - 1]) + prices[j] - prices[j - 1]
                dp[i][j] = max(dp[i][j - 1], local[i][j])

        return dp[k][len(prices) - 1]


if __name__ == "__main__":

    sol = Solution()
    method = sol.maxProfit

    cases = [
        # (method, (1, [1,2]), 1),
        # (method, (2, [2,4,1]), 2),
        # (method, (2, [3,2,6,5,0,3]), 7),
        (method, (2, [6,1,3,2,4,7]), 7),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))