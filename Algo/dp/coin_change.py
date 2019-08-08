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
        mem = {}
        self.cc(coins, mem, amount)
        return mem.get(amount, -1)

    def cc(self, coins, mem, n):
        if n in mem:
            return mem[n]

        if n <= 0:
            return 0

        res = 1 + self.cc(coins, mem, n-coins[0])
        for i in range(1, len(coins)):
            m = self.cc(coins, mem, n - coins[i])
            if res > m:
                res = m
        mem[n] = res


if __name__ == '__main__':

    sol = Solution()
    method = sol.coinChange

    cases = [
        (method, ([1, 2, 5], 11), 3),
        (method, ([2], 3), -1),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))