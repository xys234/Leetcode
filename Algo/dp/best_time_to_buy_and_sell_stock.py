"""
121. Best Time to Buy and Sell Stock (Easy)

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

Review:
2019-06-20

"""

class Solution:
    def maxProfit_Slow(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_id = 0
        profit = 0
        decrease_sorted = True
        increase_sorted = True
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] < prices[min_id]:
                    min_id = j
                if prices[j] > prices[j-1]:
                    decrease_sorted = False
                if prices[j] < prices[j-1]:
                    increase_sorted = False
                change = prices[j] - prices[i]
                if change > profit:
                    profit = change
            if increase_sorted:
                return prices[-1] - prices[0]
            if i > min_id or decrease_sorted:
                break
        return profit

    def maxProfit(self, prices):
        min_price, max_profit = float("inf"), 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p - min_price, max_profit)
        return max_profit

    def maxProfit2(self, prices):
        lowest_price, max_profit = prices[0], 0
        for k in range(1, len(prices)):
            if prices[k] > lowest_price and max_profit < prices[k] - lowest_price:
                max_profit = prices[k] - lowest_price
            elif prices[k] < lowest_price:
                lowest_price = prices[k]
        return max_profit


if __name__ == "__main__":

    sol = Solution()
    method = sol.maxProfit2

    cases = [
        (method, ([7, 1, 5, 3, 6, 4],), 5),
        (method, ([7, 6, 4, 3, 1],), 0),
        (method, ([3,3,5,0,0,3,1,4],), 4),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))