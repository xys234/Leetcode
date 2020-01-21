"""

494. Target Sum

Medium


You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

History:
2019.07.24

"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s, n = sum(nums), len(nums)
        if s < S:
            return 0

        dp = {(0, 0): 1}
        cumu_sum = 0
        for i in range(1, n+1):
            num = nums[i-1]
            cumu_sum += num
            for j in range(-cumu_sum-1, cumu_sum+1):
                ways = dp.get((i-1, j-num), 0) + dp.get((i-1, j+num), 0)
                if ways != 0:
                    dp[(i, j)] = ways

        return dp.get((n, S), 0)

    def findTargetSumWays_solution(self, nums: List[int], S: int) -> int:
        y=sum(nums)
        if y<S or ((y+S)%2==1):
            return 0
        w=(y+S)//2
        dp=[0]*(w+1)
        dp[0]=1
        for num in nums:
            for i in reversed(range(num,w+1)):
                dp[i]=dp[i]+dp[i-num]
        return dp[w]

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        n = len(nums)
        total = sum(nums)

        if S > total or S < -total:
            return 0

        dp = [[0] * (2 * total + 1) for _ in range(n)]

        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, n):
            for k in range(-total, total + 1):
                if dp[i - 1][k + total] > 0:
                    dp[i][k + nums[i] + total] += dp[i - 1][k + total]
                    dp[i][k - nums[i] + total] += dp[i - 1][k + total]
        return dp[-1][S + total]

if __name__ == '__main__':

    sol = Solution()
    method = sol.findTargetSumWays

    cases = [
        # (method, ([1, 1, 1, 1, 1], 3), 5),
        (method, ([1, 0], 1), 2),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))