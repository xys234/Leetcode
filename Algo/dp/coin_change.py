"""

322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1


"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if amount < 0:
            return -1

        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for m in range(1, amount+1):
            for coin in coins:
                if coin <= m:
                    dp[m] = min(dp[m], 1+dp[m-coin])
        if dp[amount] > amount:
            return -1
        return dp[amount]

    def coinChange_topdown(self, coins: List[int], amount: int) -> int:
        mem = {0:0}
        self.cc(coins, mem, amount)
        return mem.get(amount, -1)

    def cc(self, coins, mem, n):
        if n in mem:
            return mem[n]

        if n < 0:
            return -1

        res = self.cc(coins, mem, n-coins[0])
        if res >= 0:
            res += 1
        for i in range(1, len(coins)):
            m = self.cc(coins, mem, n - coins[i])
            if m >= 0 and res == -1 or (m >= 0 and m + 1 < res):
                res = m + 1
        if res >= 0:
            mem[n] = res
        else:
            mem[n] = -1
        return res

    def coinChange_solution(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = 2 ** 31 - 1
        lenc = len(coins)

        def helper(current, restMoney, count):
            if not restMoney:
                self.res = min(count, self.res)
            for i in range(current, lenc):
                if coins[i] <= restMoney < coins[i] * (self.res - count):
                    helper(i, restMoney - coins[i], count + 1)

        for i in range(lenc):
            helper(i, amount, 0)

        return self.res if self.res < 2 ** 31 - 1 else -1


if __name__ == '__main__':

    sol = Solution()
    method = sol.coinChange_solution_topdown

    cases = [
        (method, ([1, 2, 5], 11), 3),
        (method, ([2], 3), -1),
        (method, ([1], 0), 0),
        (method, ([2], 1), -1),
        (method, ([2,5,1], 6), 2),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))