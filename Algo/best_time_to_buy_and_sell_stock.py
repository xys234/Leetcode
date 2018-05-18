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

if __name__=="__main__":
    sol = Solution()
    # p1 = [7, 1, 5, 3, 6, 4]
    # print(sol.maxProfit(p1))

    p2 = list(range(10000,0,-1))
    p2.extend([0]*10000)
    print(sol.maxProfit(p2))